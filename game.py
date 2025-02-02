import streamlit as st
import pandas as pd
import random
import time

def safe_rerun():
    if hasattr(st, "experimental_rerun"):
        st.experimental_rerun()
    elif hasattr(st, "rerun"):
        st.rerun()
    else:
        raise Exception("Streamlit rerun function not found. Please update Streamlit.")

def load_words(filename="words.csv"):
    df = pd.read_csv(filename)
    return df["words"].tolist()

if "score" not in st.session_state:
    st.session_state.score = {"Team 1": 0, "Team 2": 0}
if "current_team" not in st.session_state:
    st.session_state.current_team = "Team 1"
if "words_queue" not in st.session_state:
    st.session_state.words_queue = [] 
if "words" not in st.session_state:
    st.session_state.words = load_words()
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
if "time_up" not in st.session_state:
    st.session_state.time_up = False

st.set_page_config(page_title="Astronomy Taboo Game", layout="wide")
st.title("🌌 Astronomy Taboo Game 🌠")
st.markdown("---")

def start_new_round():
    st.session_state.words_queue = random.sample(st.session_state.words, st.session_state.round_words)
    st.session_state.round_started = True
    st.session_state.start_time = time.time()
    st.session_state.time_up = False

def end_round():
    st.session_state.round_summary.append({
         "team": st.session_state.team_names[st.session_state.current_team],
         "score": st.session_state.score[st.session_state.current_team]
    })
    st.session_state.current_team = "Team 2" if st.session_state.current_team == "Team 1" else "Team 1"
    st.session_state.round_started = False
    st.session_state.start_time = None
    safe_rerun()

def calculate_remaining_time():
    if st.session_state.start_time:
        elapsed = time.time() - st.session_state.start_time
        return max(st.session_state.timer_duration - int(elapsed), 0)
    return st.session_state.timer_duration

if not st.session_state.game_started:
    st.sidebar.header("⚙️ Game Settings")
    team1 = st.sidebar.text_input("Team 1 Name", "Team 1")
    team2 = st.sidebar.text_input("Team 2 Name", "Team 2")
    timer_duration = st.sidebar.number_input("Round Duration (seconds)", 30, 180, 60, key="timer_input")
    round_words = st.sidebar.number_input("Words per Round", 3, 10, 5, key="round_input")

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
        if st.session_state.start_time and (time.time() - st.session_state.start_time) >= st.session_state.timer_duration:
            end_round()

        if not st.session_state.words_queue:
            end_round()

        if st.session_state.start_time:
            timer_html = f"""
            <script>
            const startTime = {st.session_state.start_time * 1000};
            const duration = {st.session_state.timer_duration * 1000};
            function updateTimer() {{
                const currentTime = Date.now();
                const elapsed = currentTime - startTime;
                const remaining = Math.max(duration - elapsed, 0);
                let displayText = remaining > 0 ? Math.floor(remaining/1000) + "s" : "";
                document.getElementById('countdown').textContent = displayText;
                if (remaining <= 0) {{
                    clearInterval(timerInterval);
                    setTimeout(function() {{
                        window.parent.document.getElementById('auto_end_round').click();
                    }}, 1000);
                }}
            }}
            const timerInterval = setInterval(updateTimer, 100);
            updateTimer();
            </script>
            <div id="countdown" style="font-size:24px; font-weight:bold; text-align:center;"></div>
            """
            st.components.v1.html(timer_html, height=50)

        if st.session_state.words_queue:
            current_word = st.session_state.words_queue[0]
        else:
            current_word = "🎉 All words completed!"
        st.markdown(f"""
        <div style="border: 2px solid #4a4a4a; border-radius: 10px; padding: 30px; 
                    text-align: center; font-size: 36px; font-weight: bold; color:blue;
                    margin: 20px 0; background: #f8f9fa;">
            {current_word}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <style>
            /* Sadece bu iki buton için özel stil */
            [data-testid="baseButton-correct_guess"],
            [data-testid="baseButton-skip"] {
                padding: 25px 35px !important;
                font-size: 24px !important;
                border-radius: 15px !important;
                width: 100% !important;
                margin-bottom: 10px;
            }
        </style>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Correct", use_container_width=True, key="correct_guess"):
                # Mevcut iş mantığı
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

    st.sidebar.markdown("---")
    st.sidebar.subheader("🏆 Scoreboard")
    for team in ["Team 1", "Team 2"]:
        st.sidebar.metric(
            st.session_state.team_names[team],
            st.session_state.score[team]
        )

    if st.session_state.round_summary:
        st.sidebar.markdown("### 📊 Round Summaries")
        for summary in st.session_state.round_summary[-3:]:
            st.sidebar.write(f"- {summary['team']}'s round completed with {summary['score']} points.")

    if st.sidebar.button("🔄 Reset Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        safe_rerun()
