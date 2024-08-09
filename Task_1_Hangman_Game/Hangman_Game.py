import random
from ANSII import ANSIColor


def choose_word():
    words = ["codealpha", "python", "programming", "computer", "science", "algorithm", "database", "network"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def update_lives(lives):
    return ANSIColor.format_text(str(lives), color='bright_red', bg_color='black', style='bold')

def hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()

    lives = 6
    colored_lives = update_lives(lives)

    welcome_text = ">>> Welcome to Hangman!"
    colored_welcome = ANSIColor.format_text(welcome_text, color='red', bg_color='bright_white', style='bold')
    print(colored_welcome)

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {colored_lives} lives left.")
        print("Letters used:", ' '.join(guessed_letters))
        print("Current word:", display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1
                colored_lives = update_lives(lives)
                print("Letter is not in the word.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
        else:
            print("Invalid character. Please enter a letter.")

    Coloured_Word = ANSIColor.format_text(str(word), color='bright_white', bg_color='bright_green', style='bold')
    if lives == 0:
        print(f"Sorry, you died. The word was {Coloured_Word}")
    else:
        print(f"Congratulations! You guessed the word {Coloured_Word}!")

if __name__ == "__main__":
    hangman()