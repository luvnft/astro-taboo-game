<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Astronomy Taboo Game</title>
    <style>
        body {
            font-family: "Helvetica Neue", Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
            color: #333;
        }
        h1, h2, h3 {
            margin-bottom: 10px;
        }
        h1 {
            font-size: 2.2em;
            margin-top: 0;
        }
        p, li {
            font-size: 1em;
        }
        code {
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        .note {
            background: #fef7e0;
            border-left: 4px solid #ffc107;
            padding: 10px;
            margin: 1em 0;
        }
        .desc {
            font-style: italic;
            margin-bottom: 1em;
        }
        ul {
            margin: 10px 0 20px 40px;
        }
        ol {
            margin: 10px 0 20px 40px;
        }
        .footer {
            margin-top: 30px;
            font-size: 0.9em;
            color: #777;
        }
        .footer a {
            color: #337ab7;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>Astronomy Taboo Game</h1>
    
    <p class="desc">
        A thrilling, astronomy-themed word-guessing game where players try to get their teams 
        to say the main word without using the forbidden (taboo) clues.
    </p>

    <p>
        This application is built with <strong>Streamlit</strong> and hosts a set of astronomy-related words 
        and their taboo clues from a simple CSV file. It is designed to be played in real-time with multiple teams.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Multi-team Setup:</strong> Choose how many teams will play.</li>
        <li><strong>Round Timer & Word Count:</strong> Customize the duration of each round and how many words appear per round.</li>
        <li><strong>Scoreboard & Round History:</strong> Track each team's points and review previous rounds.</li>
        <li><strong>Interactive Gameplay:</strong> Mark words as correct, skipped, or tabooed — the scores update automatically.</li>
        <li><strong>Shuffle & Replay:</strong> Randomly shuffles words to keep the game fresh for repeated plays.</li>
    </ul>

    <h2>How It Works</h2>
    <ol>
        <li>Open the game at: <a href="https://astro-taboo-game.streamlit.app/" target="_blank">https://astro-taboo-game.streamlit.app/</a>.</li>
        <li>Configure the basic settings:
            <ul>
                <li><em>Number of Teams</em></li>
                <li><em>Round Duration</em> (in seconds)</li>
                <li><em>Words per Round</em></li>
            </ul>
        </li>
        <li>Enter each team's name.</li>
        <li>Click <strong>Start Game</strong> to begin.</li>
        <li>When it’s your team’s turn:
            <ul>
                <li>Press <code>Start Round</code> and the timer will begin.</li>
                <li>The main word and its forbidden clues will appear on-screen.</li>
                <li>Describe the word without using the taboo clues.</li>
            </ul>
        </li>
        <li>Use the action buttons to mark:
            <ul>
                <li><strong>Correct</strong>: +1 point</li>
                <li><strong>Skip</strong>: Moves the word to the end of the queue (no points gained or lost)</li>
                <li><strong>Taboo</strong>: -1 point (if a forbidden word is mentioned)</li>
            </ul>
        </li>
        <li>Repeat until the timer runs out or all words for that round are done.</li>
        <li>Check the <strong>Scoreboard</strong> and <strong>Round History</strong> to see how each team performed.</li>
        <li>Continue with the next team and repeat more rounds for as long as you like!</li>
    </ol>

    <h2>CSV Structure</h2>
    <p>
        This application reads words from a CSV file with the following columns:
    </p>
    <ul>
        <li><strong>words</strong> – The main word to be guessed.</li>
        <li><strong>taboo1</strong>, <strong>taboo2</strong>, <strong>taboo3</strong> – The forbidden words associated with the main word.</li>
    </ul>
    <p>
        For example:
    </p>
    <pre><code>
words,taboo1,taboo2,taboo3
Galaxy,Stars,Cluster,Spiral
Black Hole,Gravity,Collapse,Event Horizon
Exoplanet,Orbit,Habitable,Alien
    </code></pre>

    <h2>Local Usage (Optional)</h2>
    <p>
        If you want to run the game locally, you can clone the repository, navigate to its folder, and use Streamlit:
    </p>
    <ol>
        <li>Install the necessary requirements: 
            <br><code>pip install -r requirements.txt</code></li>
        <li>Run the application:
            <br><code>streamlit run app.py</code></li>
        <li>Open the provided local URL in your web browser to start playing.</li>
    </ol>

    <h2>Contributing</h2>
    <p>
        Contributions are welcome! Feel free to fork this project and submit pull requests with new words, features, or improvements.
    </p>

    <div class="note">
        <strong>Tip:</strong> You can enhance the game by updating the CSV file with additional astronomy-related words and taboo clues.
        This helps keep the game fresh and challenging.
    </div>

    <div class="footer">
        <hr />
        <p>
            Created by <strong>Your Name</strong> | 
            <a href="https://astro-taboo-game.streamlit.app/" target="_blank">Live Demo</a>
        </p>
    </div>
</body>
</html>
