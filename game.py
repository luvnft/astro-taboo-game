import streamlit as st
import pandas as pd
import random
import time
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Astronomy Taboo Game", layout="centered")


def safe_rerun():
    st.rerun() if hasattr(st, "rerun") else st.experimental_rerun()


def load_words():
    try:
        df = pd.read_csv("test_words.csv")
        words = [
            {
                "main_word": row["words"],
                "taboos": [str(row[f"taboo{i}"]) for i in range(1, 4) if pd.notna(row[f"taboo{i}"])]
            } for _, row in df.iterrows()
        ]
        random.shuffle(words)
        return words
    except Exception as e:
        st.error(f"Error loading words: {str(e)}")
        return []


# Session state initialization
if 'words' not in st.session_state:
    st.session_state.words = load_words()

defaults = {
    "score": {},
    "current_team": 0,
    "words_queue": [],
    "remaining_words": [],
    "team_names": {},
    "game_started": False,
    "round_started": False,
    "start_time": None,
    "round_summary": [],
    "timer_duration": 60,
    "round_words": 5,
    "team_count": 2,
    "words_processed": 0,
    "taboo_count": 0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.markdown(
    """
    <style>

        .main-title {
            text-align: center;
            margin: 0 0 25px 0 !important;
            font-size: 3em !important;
            padding: 5px;
            letter-spacing: 1px;
            font-weight: 700;
            font-family: 'Helvetica', sans-serif;            
        }
        /* Round History margin adjustment */
        .round-history-header {
            margin: 25px 0 15px 0 !important;
        }

        /* Score card spacing */
        .score-card {
            margin-bottom: 25px !important;
        }

        .score-card {
            background: linear-gradient(145deg, #2b5876, #4e4376);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 5px;
            color: white;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
            text-align: center; /* Yeni eklendi */
            display: flex; /* Yeni eklendi */
            flex-direction: column; /* Yeni eklendi */
            justify-content: center; /* Yeni eklendi */
            min-height: 120px; /* Yeni eklendi */
        }

        .score-card:hover {
            transform: translateY(-3px);
        }

        .timer-box {
            text-align: center;
            margin: 10px 0;
            padding: 20px;
            background: linear-gradient(145deg, #2b5876, #4e4376);
            border-radius: 15px;
            color: white;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .stButton>button {
            transition: all 0.3s ease;
            transform: scale(1);
            border: 3px solid #4e4376 !important;
        }

        .stButton>button:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 5px 15px rgba(78, 67, 118, 0.3) !important;
        }

        /* Mevcut CSS içine ekle */
        .action-buttons .stButton > button {
            height: 150px !important;
            font-size: 26px !important;
            padding: 25px 35px !important;
            border-radius: 18px !important;
            margin: 8px 0;
        }

        .team-input input {
            font-size: 16px !important;
            padding: 12px !important;
            border-radius: 8px !important;
        }

        .round-history-container::-webkit-scrollbar {
            width: 8px;
        }


        .round-history-container::-webkit-scrollbar-track {
            background: rgba(78, 67, 118, 0.05);
            border-radius: 4px;
        }

        .round-history-container::-webkit-scrollbar-thumb {
            background: rgba(78, 67, 118, 0.3);
            border-radius: 4px;
        }

        .round-history-container::-webkit-scrollbar-thumb:hover {
            background: rgba(78, 67, 118, 0.5);
        }        

       .round-summary-item {
            transition: all 0.2s ease;
            border-left: 4px solid #4e4376;
            padding: 10px;
            margin: 8px 0;
            background: rgba(255,255,255,0.05);
            border-radius: 4px;
            font-size: 15px;
        }
        .round-summary-item:hover {
            transform: translateX(5px);
            background: rgba(78, 67, 118, 0.15) !important;
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(78, 67, 118, 0.05);
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(78, 67, 118, 0.3);
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(78, 67, 118, 0.5);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">Astronomy Taboo</div>', unsafe_allow_html=True)


def initialize_teams():
    st.session_state.score = {i: 0 for i in range(st.session_state.team_count)}
    st.session_state.remaining_words = st.session_state.words.copy()
    random.shuffle(st.session_state.remaining_words)
    st.session_state.words_processed = 0
    st.session_state.taboo_count = 0


def start_new_round():

    remaining = st.session_state.remaining_words.copy()
    random.shuffle(remaining)

    while len(remaining) < st.session_state.round_words:
        remaining += st.session_state.words.copy()

    selected_words = remaining[:st.session_state.round_words]

    st.session_state.remaining_words = remaining[st.session_state.round_words:]

    st.session_state.words_queue = selected_words
    st.session_state.words_processed = 0
    st.session_state.taboo_count = 0
    st.session_state.round_started = True
    st.session_state.start_time = time.time()
    safe_rerun()


def end_round():
    duration = min(time.time() - st.session_state.start_time, st.session_state.timer_duration)
    current_team = st.session_state.current_team

    st.session_state.round_summary.append({
        "round_number": len(st.session_state.round_summary) + 1,
        "team": st.session_state.team_names[current_team],
        "score": st.session_state.words_processed - st.session_state.taboo_count,
        "taboos": st.session_state.taboo_count,
        "duration": f"{int(duration)}s"
    })

    st.session_state.current_team = (current_team + 1) % st.session_state.team_count
    st.session_state.round_started = False
    st.session_state.start_time = None
    safe_rerun()


# Game Setup
if not st.session_state.game_started:
    with st.container():
        st.markdown("### 🚀 Game Setup")
        cols = st.columns(3)
        with cols[0]:
            team_count = st.number_input("Number of Teams", 2, 6, value=st.session_state.team_count)
        with cols[1]:
            timer_duration = st.number_input("Round Duration (s)", 30, 180, value=st.session_state.timer_duration)
        with cols[2]:
            round_words = st.number_input("Words per Round", 3, 10, value=st.session_state.round_words)

        st.markdown("---")
        st.markdown("### 👥 Team Configuration")
        team_cols = st.columns(team_count)
        team_names = {}
        for i in range(team_count):
            with team_cols[i]:
                team_names[i] = st.text_input(
                    f"Team {i + 1} Name",
                    value=st.session_state.team_names.get(i, f"Team {i + 1}"),
                    key=f"team_{i}"
                ).strip()

        st.markdown("---")
        if st.button("🎮 Start Game", use_container_width=True, type="primary"):
            st.session_state.team_count = team_count
            st.session_state.timer_duration = timer_duration
            st.session_state.round_words = round_words
            st.session_state.team_names = team_names
            initialize_teams()
            st.session_state.game_started = True
            safe_rerun()

else:
    with st.container():
        # Scoreboard
        st.markdown("### 🏆 Scoreboard")
        cols = st.columns(st.session_state.team_count)
        for team_id in range(st.session_state.team_count):
            with cols[team_id]:
                st.markdown(f"""
                    <div class="score-card">
                        <div style="font-size: 1.1em; margin-bottom: 10px; text-align: center;">
                            {st.session_state.team_names[team_id]}
                        </div>
                        <div style="font-size: 1.8em; font-weight: bold; text-align: center;">
                            {st.session_state.score[team_id]}
                        </div>
                    </div>
                """, unsafe_allow_html=True)


        if not st.session_state.round_started and st.session_state.round_summary:
            st.markdown("---")
            st.markdown("### 📊 Round History")

            history_html = """
            <div class="round-history-container" style="
                max-height: 200px;
                overflow-y: auto;
                padding: 10px;
                border-radius: 8px;
                border: 2px solid rgba(78, 67, 118, 0.2);
                margin-bottom: 20px;
            ">
            """

            for summary in reversed(st.session_state.round_summary):
                history_html += (
                    f'<div class="round-summary-item">'
                    f'<b>Round {summary["round_number"]}</b> ({summary["team"]})<br>'
                    f'⭐ {summary["score"]} | 🚫 {summary["taboos"]} | ⏱️ {summary["duration"]}'
                    f'</div>'
                )

            history_html += "</div>"

            st.markdown(history_html, unsafe_allow_html=True)

        if not st.session_state.round_started:
            st.markdown("---")
            st.markdown(f"### ⏭️ Next Team: **{st.session_state.team_names[st.session_state.current_team]}**")
            if st.button("⏱️ Start Round", use_container_width=True, type="primary"):
                start_new_round()

if st.session_state.game_started and st.session_state.round_started:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, st.session_state.timer_duration - elapsed)
    st_autorefresh(interval=1000, key="timer_refresh")

    if remaining <= 0 or st.session_state.words_processed >= st.session_state.round_words:
        end_round()
    else:
        st.markdown(f"""
        <div class="timer-box">
            <div style="font-size: 18px; margin-bottom: 8px;">⏳ Remaining Time</div>
            <div style="font-size: 36px; font-weight: 800;">
                {int(remaining)}<span style="font-size: 20px">s</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        current_word = st.session_state.words_queue[0] if st.session_state.words_queue else {"main_word": "Game Over!",
                                                                                             "taboos": []}

        st.markdown(f"""
        <div style="margin: 20px 0; padding: 25px; background: #2b5876;
            border-radius: 15px; color: white; text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: 2px solid #4e4376;">
            <div style="font-size: 32px; font-weight: bold; margin-bottom: 25px;">
                {current_word['main_word']}
            </div>
            <div style="font-size: 20px;">
                🚫 Taboo Words:
                <div style="margin-top: 15px; line-height: 1.6;">
                    {'<br>'.join(current_word['taboos'])}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("✅ Correct", key="correct", type="primary", use_container_width=True):
                st.session_state.score[st.session_state.current_team] += 1
                st.session_state.words_processed += 1
                st.session_state.words_queue.pop(0)
                safe_rerun()
        with col2:
            if st.button("⏭️ Skip", key="skip", use_container_width=True):
                st.session_state.words_queue.append(st.session_state.words_queue.pop(0))
                safe_rerun()
        with col3:
            if st.button("🚫 Taboo", key="taboo", type="secondary", use_container_width=True):
                st.session_state.score[st.session_state.current_team] -= 1
                st.session_state.words_processed += 1
                st.session_state.taboo_count += 1
                st.session_state.words_queue.pop(0)
                safe_rerun()
