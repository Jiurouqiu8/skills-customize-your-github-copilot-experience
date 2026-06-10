# 🎮 Hangman Game Challenge

## 🎯 Objective

Build a Python Hangman game that uses strings, loops, and user input to let a player guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Create the Hangman game logic

#### Description
Implement the core game mechanics so the program randomly selects a word, accepts player guesses, and displays progress as letters are revealed.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses from the player
- Display the current word progress using blanks and revealed letters
- Track and show remaining incorrect guesses
- Reveal the full word when the game ends

### 🛠️ Add game flow and winning/losing messages

#### Description
Build the game flow so the player can continue guessing until they win or lose, and show a clear result message.

#### Requirements
Completed program should:

- End the game when the word is guessed or attempts are exhausted
- Display a win message when the player guesses the word
- Display a lose message when the player runs out of guesses
- Prevent duplicate counting for repeated correct letters
