import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'algorithm', 'function']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while tries > 0 and set(word) != guessed_letters:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in word:
            print("Correct!")
            guessed_letters.add(guess)
        else:
            print("Wrong!")
            tries -= 1

        print(display_word(word, guessed_letters))
        print(f"Tries left: {tries}")

    if set(word) == guessed_letters:
        print("Congratulations! You guessed the word:", word)
    else:
        print("You lost! The word was:", word)

if __name__ == "__main__":
    hangman()