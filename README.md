
# Astronomy Taboo Game

*An interactive application built with Python and Streamlit, where players guess astronomy-themed words without using any forbidden clues.*

---

## Overview

The **Astronomy Taboo Game** is a fun and challenging multiplayer experience where you and your friends attempt to describe astronomy-related words without using certain "taboo" hints. It leverages **Python** for its logic, **Streamlit** for the user interface, and a **CSV** file for storing the words and their forbidden clues.

---

## Features

- **Multiple Teams**: Configure how many teams will participate and name each one.
- **Customizable Rounds**: Define the duration of each round (in seconds) and the number of words per round.
- **Live Score Tracking**: The score automatically updates whenever a team scores a point or incurs a penalty.
- **Round History**: View a summary of past rounds, including each team's score and any taboo violations.
- **Easy-to-Update Word List**: Add or modify words and their forbidden clues by editing a single CSV file.

---

## How to Play

1. **Access the Live Application**:  
   Visit [https://astro-taboo-game.streamlit.app/](https://astro-taboo-game.streamlit.app/).
2. **Set Game Parameters**:
   - Number of teams
   - Round duration (in seconds)
   - Number of words per round
3. **Assign Team Names**:  
   Enter the names for each team and click **Start Game**.
4. **Gameplay**:
   - A main word appears along with up to three forbidden (taboo) clues.
   - Describe the main word to your team without using any of the forbidden clues.
   - Use the buttons to mark the guess as **Correct** (+1 point), **Skip** (no change), or **Taboo** (-1 point penalty).
5. **Check Results**:  
   Scores update automatically at the end of each round, and you can review the round history.
6. **Continue Play**:  
   Proceed to the next team’s turn and keep playing as many rounds as you like.

---

## CSV Format

A standard CSV file is used to supply words and their forbidden clues.  
The file should have the following columns:

```csv
words,taboo1,taboo2,taboo3
Planet,Orbit,Revolve,Star
Galaxy,Spiral,Cluster,Stars
Black Hole,Gravity,Collapse,Event Horizon
```

---

## Optional: Run Locally

If you wish to run the game locally:

1. **Clone the Repository** or download the source code.
2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Launch the App**:
    ```bash
    streamlit run app.py
    ```
4. **Open the Local URL**: 
   Streamlit will provide a local URL. Open it in your browser to start playing.

---

## Contributing

Contributions and suggestions are welcome. You can enhance the gameplay, add more words to the CSV file, or improve the user interface. To get started, fork this repository and submit your pull requests.

---

*Enjoy exploring the cosmos, one word at a time!*
