<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Astronomy Taboo Game</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      margin: 0;
      padding: 0;
      line-height: 1.6;
    }
    h1, h2, h3 {
      color: #333;
    }
    pre {
      background: #eee;
      padding: 10px;
      overflow-x: auto;
    }
    code {
      font-family: Consolas, "Courier New", monospace;
    }
    a {
      color: #007acc;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    hr {
      margin: 20px 0;
      border: none;
      border-top: 1px solid #ddd;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Astronomy Taboo Game</h1>
    <p><em>An interactive application built with Python and Streamlit, where players guess astronomy-themed words without using any forbidden clues.</em></p>
    
    <hr />

    <h2>Overview</h2>
    <p>
      The <strong>Astronomy Taboo Game</strong> is a fun and challenging multiplayer experience where you and your friends attempt to describe astronomy-related words without using certain "taboo" hints. It leverages <strong>Python</strong> for its logic, <strong>Streamlit</strong> for the user interface, and a <strong>CSV</strong> file for storing the words and their forbidden clues.
    </p>
    
    <hr />

    <h2>Features</h2>
    <ul>
      <li><strong>Multiple Teams</strong>: Configure how many teams will participate and name each one.</li>
      <li><strong>Customizable Rounds</strong>: Define the duration of each round (in seconds) and the number of words per round.</li>
      <li><strong>Live Score Tracking</strong>: The score automatically updates whenever a team scores a point or incurs a penalty.</li>
      <li><strong>Round History</strong>: View a summary of past rounds, including each team's score and any taboo violations.</li>
      <li><strong>Easy-to-Update Word List</strong>: Add or modify words and their forbidden clues by editing a single CSV file.</li>
    </ul>
    
    <hr />

    <h2>How to Play</h2>
    <ol>
      <li>
        <strong>Access the Live Application</strong>:  
        Visit <a href="https://astro-taboo-game.streamlit.app/" target="_blank">https://astro-taboo-game.streamlit.app/</a>.
      </li>
      <li>
        <strong>Set Game Parameters</strong>:
        <ul>
          <li>Number of teams</li>
          <li>Round duration (in seconds)</li>
          <li>Number of words per round</li>
        </ul>
      </li>
      <li>
        <strong>Assign Team Names</strong>:  
        Enter the names for each team and click <strong>Start Game</strong>.
      </li>
      <li>
        <strong>Gameplay</strong>:
        <ul>
          <li>A main word appears along with up to three forbidden (taboo) clues.</li>
          <li>Describe the main word to your team without using any of the forbidden clues.</li>
          <li>Use the buttons to mark the guess as <strong>Correct</strong> (+1 point), <strong>Skip</strong> (no change), or <strong>Taboo</strong> (-1 point penalty).</li>
        </ul>
      </li>
      <li>
        <strong>Check Results</strong>:  
        Scores update automatically at the end of each round, and you can review the round history.
      </li>
      <li>
        <strong>Continue Play</strong>:  
        Proceed to the next team’s turn and keep playing as many rounds as you like.
      </li>
    </ol>
    
    <hr />

    <h2>CSV Format</h2>
    <p>A standard CSV file is used to supply words and their forbidden clues. The file should have the following columns:</p>
    <pre><code>words,taboo1,taboo2,taboo3
Planet,Orbit,Revolve,Star
Galaxy,Spiral,Cluster,Stars
Black Hole,Gravity,Collapse,Event Horizon</code></pre>
    
    <hr />

    <h2>Optional: Run Locally</h2>
    <p>If you wish to run the game locally:</p>
    <ol>
      <li><strong>Clone the Repository</strong> or download the source code.</li>
      <li>
        <strong>Install Dependencies</strong>:
        <pre><code>pip install -r requirements.txt</code></pre>
      </li>
      <li>
        <strong>Launch the App</strong>:
        <pre><code>streamlit run app.py</code></pre>
      </li>
      <li>
        <strong>Open the Local URL</strong>: 
        Streamlit will provide a local URL. Open it in your browser to start playing.
      </li>
    </ol>
    
    <hr />

    <h2>Contributing</h2>
    <p>
      Contributions and suggestions are welcome. You can enhance the gameplay, add more words to the CSV file, 
      or improve the user interface. To get started, fork this repository and submit your pull requests.
    </p>
    
    <hr />

    <p><em>Enjoy exploring the cosmos, one word at a time!</em></p>
  </div>
</body>
</html>
