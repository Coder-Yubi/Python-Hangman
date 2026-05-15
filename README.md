# Python-Hangman
A feature-rich Hangman game built with Python and Pygame, featuring dynamic difficulty logic, real-time health tracking, and immersive audio effects.
<h1 align="center">🎮 Hangman: Python Edition 🐍</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Library-Pygame-green?style=for-the-badge" alt="Library">
</p>

<hr>

<!-- Project Overview Section -->
<h2>📝 Project Overview</h2>
<p>
  This is a modern take on the classic <b>Hangman game</b>, developed using Python. Unlike standard terminal games, this version integrates the <code>Pygame</code> library to provide a rich multimedia experience with background music and reactive sound effects.
</p>
<p>
  The game logic is designed to be beginner-friendly yet challenging, using a <b>dynamic hint system</b> that balances the difficulty based on the word length.
</p>

<hr>

<!-- Features Section using a Table for better alignment -->
<h2>✨ Key Features</h2>

<table width="100%">
  <tr>
    <td><b>🔊 Multimedia Integration</b></td>
    <td>Uses <code>pygame.mixer</code> for high-quality audio feedback (Correct/Wrong/Win/Loss).</td>
  </tr>
  <tr>
    <td><b>🎯 Smart Difficulty</b></td>
    <td>Automatically reveals approx 50% of the word as a starting hint to keep gameplay engaging.</td>
  </tr>
  <tr>
    <td><b>❤️ Visual Health System</b></td>
    <td>A dynamic life tracker using emojis and ASCII art to represent remaining attempts.</td>
  </tr>
  <tr>
    <td><b>🛡️ Robust Logic</b></td>
    <td>Handles edge cases like duplicate letters, case sensitivity, and invalid inputs.</td>
  </tr>
  <tr>
    <td><b>🎮 ASCII UI</b></td>
    <td>Features custom ASCII banners for a retro "hacker" terminal aesthetic.</td>
  </tr>
</table>

<hr>

<!-- Installation Section -->
<h2>🚀 Getting Started</h2>

<p>To run this game locally, follow these steps:</p>

<ol>
  <li>Clone the repository</li>
  <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
  <li>Run the script: <code>python hangman.py</code></li>
</ol>
