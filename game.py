import streamlit as st
import pandas as pd
import random
import time
from streamlit_autorefresh import st_autorefresh

def safe_rerun():
    if hasattr(st, "experimental_rerun"):
        st.experimental_rerun()
    elif hasattr(st, "rerun"):
        st.rerun()

def load_words(filename="deneme.csv"):
    try:
        df = pd.read_csv(filename)
        words_list = []
        for _, row in df.iterrows():
            main_word = row["words"]
            taboos = [str(row[f"taboo{i}"]) for i in range(1,4) if pd.notna(row.get(f"taboo{i}", ""))]
            words_list.append({"main_word": main_word, "taboos": taboos})
        return words_list
    except FileNotFoundError:
        st.error("Words file not found! Please create a 'deneme.csv' file.")
        return []

if "score" not in st.session_state:
    st.session_state.score = {"Team 1": 0, "Team 2": 0}
if "current_team" not in st.session_state:
    st.session_state.current_team = "Team 1"
if "words_queue" not in st.session_state:
    st.session_state.words_queue = []
if "words" not in st.session_state:
    st.session_state.words = load_words()
if "remaining_words" not in st.session_state:
    st.session_state.remaining_words = st.session_state.words.copy()
if "team_names" not in st.session_state:
    st.session_state.team_names = {"Team 1": "Team 1", "Team 2": "Team 2"}
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "round_started" not in st.session_state:
    st.session_state.round_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "round_summary" not in st.session_state:
    st.session_state.round_summary = []
if "timer_duration" not in st.session_state:
    st.session_state.timer_duration = 60
if "round_words" not in st.session_state:
    st.session_state.round_words = 5

st.set_page_config(page_title="Astronomy Taboo Game", layout="centered")
st.title("🌌 Astronomy Taboo Game 🌠")
st.markdown("---")

def start_new_round():
    if len(st.session_state.remaining_words) < st.session_state.round_words:
        st.session_state.remaining_words = st.session_state.words.copy()
    
    selected_words = random.sample(st.session_state.remaining_words, st.session_state.round_words)
    st.session_state.words_queue = selected_words.copy()
    
    for word in selected_words:
        st.session_state.remaining_words.remove(word)
    
    st.session_state.round_started = True
    st.session_state.start_time = time.time()

def end_round():
    st.session_state.round_summary.append({
        "team": st.session_state.team_names[st.session_state.current_team],
        "score": st.session_state.score[st.session_state.current_team]
    })
    st.session_state.current_team = "Team 2" if st.session_state.current_team == "Team 1" else "Team 1"
    st.session_state.round_started = False
    st.session_state.start_time = None
    safe_rerun()

if not st.session_state.game_started:
    st.sidebar.header("⚙️ Game Settings")
    team1 = st.sidebar.text_input("Team 1 Name", "Team 1")
    team2 = st.sidebar.text_input("Team 2 Name", "Team 2")
    timer_duration = st.sidebar.number_input("Round Duration (seconds)", 30, 180, 60)
    round_words = st.sidebar.number_input("Words per Round", 3, 10, 5)
    
    if st.sidebar.button("🎮 Start Game"):
        st.session_state.team_names = {"Team 1": team1, "Team 2": team2}
        st.session_state.game_started = True
        st.session_state.score = {"Team 1": 0, "Team 2": 0}
        st.session_state.timer_duration = timer_duration
        st.session_state.round_words = round_words
        safe_rerun()

else:
    st.sidebar.header("🎮 Controls")
    current_team_name = st.session_state.team_names[st.session_state.current_team]
    
    if not st.session_state.round_started:
        st.header("Round Summary")
        if st.session_state.round_summary:
            last_summary = st.session_state.round_summary[-1]
            st.write(f"{last_summary['team']}'s round completed with {last_summary['score']} points.")
        else:
            st.write("No round has been completed yet.")
        st.sidebar.subheader(f"Next up: {current_team_name}")
        if st.sidebar.button("⏱️ Start Round"):
            start_new_round()
            safe_rerun()
    else:
        elapsed = time.time() - st.session_state.start_time
        remaining = max(0, st.session_state.timer_duration - elapsed)

        if remaining <= 0:
            end_round()
        else:
            # Countdown Timer
            countdown_container = st.empty()
            countdown_container.markdown(f"""
            <div style="
                text-align: center;
                margin: 20px 0;
                padding: 20px;
                background: linear-gradient(145deg, #2b5876, #4e4376);
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                color: white;
            ">
                <div style="font-size: 18px; margin-bottom: 8px; opacity: 0.9;">
                    ⏳ Remaining Time
                </div>
                <div style="font-size: 36px; font-weight: 800; letter-spacing: 1px;">
                    {int(remaining)}<span style="font-size: 20px">s</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st_autorefresh(interval=1000, key="round_timer")

            # Word Display
            current_word_info = {}
            if st.session_state.words_queue:
                current_word_info = st.session_state.words_queue[0]
            else:
                current_word_info = {"main_word": "All words completed!", "taboos": []}

            current_main_word = current_word_info["main_word"]
            current_taboos = current_word_info["taboos"]

            st.markdown(f"""
            <div style="
                margin: 20px 0;
                padding: 25px;
                background: linear-gradient(145deg, #2b5876, #4e4376);
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                color: white;
                text-align: center;
            ">
                <div style="font-size: 32px; font-weight: bold; margin-bottom: 25px;">
                    {current_main_word}
                </div>
                <div style="font-size: 20px;">
                    🚫 Taboo Words:
                    <div style="margin-top: 15px; display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">
                        {''.join([f'<div style="padding: 8px 15px; background: #ff4b4b; border-radius: 8px; margin: 5px;">{taboo}</div>' for taboo in current_taboos])}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Action Buttons
            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                if st.button("✅ Correct", use_container_width=True, key="correct_guess"):
                    st.session_state.score[st.session_state.current_team] += 1
                    if st.session_state.words_queue:
                        st.session_state.words_queue.pop(0)
                    if not st.session_state.words_queue:
                        end_round()
                    else:
                        safe_rerun()
            with col2:
                if st.button("⏭️ Skip", use_container_width=True, key="skip"):
                    if st.session_state.words_queue:
                        word = st.session_state.words_queue.pop(0)
                        st.session_state.words_queue.append(word)
                    safe_rerun()
            with col3:
                if st.button("🚫 Taboo", use_container_width=True, key="taboo",
                           type="primary" if st.session_state.get("last_btn") == "taboo" else "secondary"):
                    st.session_state.score[st.session_state.current_team] -= 1
                    if st.session_state.words_queue:
                        word = st.session_state.words_queue.pop(0)
                        st.session_state.words_queue.append(word)
                    safe_rerun()

    # Scoreboard
    st.sidebar.markdown("---")
    st.sidebar.subheader("🏆 Scoreboard")
    for team in ["Team 1", "Team 2"]:
        st.sidebar.metric(
            st.session_state.team_names[team],
            st.session_state.score[team]
        )
        
    if st.session_state.round_summary:
        st.sidebar.markdown("### 📊 Last Rounds")
        for summary in st.session_state.round_summary[-3:]:
            st.sidebar.caption(f"{summary['team']}: {summary['score']} pts")

    if st.sidebar.button("🔄 Reset Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        safe_rerun()

st.markdown("""
<style>
    /* Mobile-friendly adjustments */
    @media (max-width: 768px) {
        .stButton > button {
            padding: 12px 20px !important;
            font-size: 16px !important;
            margin: 5px 0;
        }
        .stMarkdown h1 {
            font-size: 28px !important;
        }
        .stMetric {
            padding: 10px !important;
        }
    }
    
    /* Taboo words styling */
    [data-testid="stMarkdownContainer"] div[style*="flex-wrap: wrap"] > div {
        font-size: 16px !important;
    }
    
    /* Center align all content */
    .main .block-container {
        max-width: 800px;
        padding: 2rem 1rem;
    }
</style>
""", unsafe_allow_html=True)
