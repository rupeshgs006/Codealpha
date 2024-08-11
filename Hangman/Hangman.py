import random
import os

def clear_screen():
    # Clears the screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_word():
    words = ['python', 'java', 'programming', 'hangman', 'computer', 'science', 'university', 'algorithm']
    return random.choice(words)

def reveal_letters(word, num_visible):
    revealed = random.sample(word, num_visible)
    return set(revealed)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def center_text(text, width):
    return text.center(width)

def hangman():
    word = choose_word()
    guessed_letters = reveal_letters(word, max(1, len(word) // 3))  # Reveal some letters at the start
    incorrect_guesses = []
    attempts = 7
    screen_width = 50

    print("Welcome to Hangman!")
    print("Some letters have been revealed to help you start.")
    
    while attempts > 0:
        clear_screen()
        print(center_text("HANGMAN GAME", screen_width))
        print(center_text(f"Guesses left: {attempts}", screen_width))
        print(center_text(f"Incorrect guesses: {', '.join(incorrect_guesses)}", screen_width))
        print(center_text(display_word(word, guessed_letters), screen_width))
        
        guess = input(center_text("Enter a letter: ", screen_width)).lower()

        if guess in guessed_letters or guess in incorrect_guesses:
            print(center_text("You've already guessed that letter. Try again.", screen_width))
        elif guess in word:
            guessed_letters.add(guess)
            print(center_text(f"Good job! '{guess}' is in the word.", screen_width))
        else:
            incorrect_guesses.append(guess)
            attempts -= 1
            print(center_text(f"Sorry, '{guess}' is not in the word. Try again.", screen_width))

        if set(word) == guessed_letters:
            clear_screen()
            print(center_text("Congratulations!", screen_width))
            print(center_text(f"You've guessed the word: {word}", screen_width))
            break
    else:
        clear_screen()
        print(center_text("Game Over!", screen_width))
        print(center_text(f"The word was: {word}", screen_width))

if __name__ == "__main__":
    hangman()
