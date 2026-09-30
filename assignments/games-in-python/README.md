
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game in which a player guesses a hidden word one letter at a time. Practice using strings, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Word and Game State

#### Description
Choose a secret word from the provided word list and prepare the game state needed to display the player's progress.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Track the letters the player has guessed and the number of incorrect guesses.
- Display the hidden word as underscores, revealing letters that have been guessed correctly.


### 🛠️ Play a Complete Round

#### Description
Create the game loop so the player can guess letters until they reveal the word or run out of allowed incorrect guesses.

#### Requirements
Completed program should:

- Ask the player to enter a letter and update the game state based on whether it appears in the secret word.
- Keep track of incorrect guesses and show how many attempts remain.
- End the round when the player guesses the full word or reaches the maximum number of incorrect guesses.
- Display a win message when the word is guessed and a lose message that reveals the secret word when attempts run out.
