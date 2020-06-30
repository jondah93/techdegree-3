from phrasehunter.phrase import Phrase
from phrasehunter.character import Character
import random


class Game:
    def __init__(self, phrases, attempts=5):
        self.original_phrases = phrases
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.active_phrase = random.choice(self.phrases)
        self.guessed = []
        self.guesses = 0
        self.attempts = attempts

    def take_guess(self):
        """Takes a guess input and return it as a Character object if it has not already been guessed"""
        while True:
            try:
                guess = Character(input('Take a guess >>> ').lower())
                if not guess.char.isalpha() or len(guess.char) != 1:
                    print('Guess must be a letter in the alphabet.')
                    continue
                if guess.char in [char.char for char in self.guessed]:
                    print('You already guessed that!')
                    del (guess)
                else:
                    self.guessed.append(guess)
                    return guess
            except ValueError:
                print('Guess must be a single letter.')

    def print_guesses(self, phrase):
        """Returns a string with all the guesses, presented with comma separation"""
        return ','.join([guess.char for guess in self.guessed if guess.char not in phrase])

    def play_again(self):
        while True:
            answer = input('Would you like to play again? (y/n) >>> ')
            if answer.lower() == 'y':
                return True
            elif answer.lower() == 'n':
                return False
            else:
                continue

    def start_game(self):
        phrase = self.active_phrase

        while self.guesses < self.attempts:
            print(phrase.print_phrase())
            guess = self.take_guess()

            # Check if the guess was in the phrase
            for char in phrase:
                if char.char == guess.char:
                    char.update_guess(guess.char)
                    guess.in_phrase = True

            # Check if the entire phrase has been guessed
            if phrase.phrase_guessed():
                print(phrase.print_phrase())
                print('Well done, you completed the phrase with {} incorrect {}!'.format(
                    self.guesses, ('guess' if self.guesses == 1 else 'guesses')
                ))
                break

            if not guess.in_phrase:
                self.guesses += 1
                print('Incorrect guesses ({}): {}.\nYou have {} {} left.'.format(
                    self.guesses, self.print_guesses(phrase.original_phrase),
                    (self.attempts-self.guesses), ('guess' if (self.attempts-self.guesses == 1) else 'guesses')
                ))

        if self.guesses == self.attempts:
            print('The phrase was "{}"!'.format(phrase.original_phrase))

        if self.play_again():
            self.__init__(self.original_phrases)
            self.start_game()
        else:
            print('Thanks for playing!')
