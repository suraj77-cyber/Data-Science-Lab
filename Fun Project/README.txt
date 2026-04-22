🧠 Word Scramble Game

An interactive console-based game built using Python where players unscramble words across multiple levels and earn points based on performance.

🚀 Overview

This game challenges players to guess the correct word from a scrambled version within a limited number of attempts.
As the player progresses, the difficulty increases with longer and more complex words.

🎮 Features
🔤 Multiple levels with increasing word complexity
🧠 Smart hints (first letter / category clues)
🏆 Score system based on remaining attempts
🔄 Replay option after game over
💻 Clean terminal interface with screen refresh
⚙️ How It Works
The game starts at Level 1
Each level includes:
A scrambled word
Limited attempts
Player guesses the correct word:
❌ Wrong guess → try again
💡 Hint option (may reduce score)
✅ Correct guess → next level
Points are awarded based on remaining attempts
Game ends when:
🎉 All levels are completed
❌ Attempts run out
🧩 Levels Configuration
Level	Word Length	Attempts	Difficulty
1	3–4 letters	4	Easy
2	4–5 letters	5	Medium
3	5–6 letters	6	Medium+
4	6–8 letters	7	Hard
5	8+ letters	8	Expert
🛠 Tech Stack
Python 🐍
Built-in Libraries:
random (word selection & scrambling)
os (clear terminal screen)
time (delay effects)
▶️ Getting Started
Prerequisites
Python 3.x installed
Run the Game
git clone https://github.com/your-username/word-scramble-game.git
cd word-scramble-game
python word_scramble_game.py
💡 Example Gameplay
Scrambled Word: ETLPA
Your Guess: plate
Correct! 🎉
📂 Project Structure
word-scramble-game/
│
├── word_scramble_game.py
├── words.txt (optional word list)
└── README.md
🔥 Future Improvements
Add word categories (Animals, Tech, Movies)
Timer-based challenge ⏱
Multiplayer mode 👥
Leaderboard system 🏆
GUI version (Tkinter / Web App)
🤝 Contributing
Author
Suraj Nair

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
