class Character:
    def __init__(self, char):
        if len(char) != 1:
            raise ValueError('Only single characters are allowed')
        if not isinstance(char, str):
            raise ValueError('Characters must be letters')
        self.char = char
        self.was_guessed = True if char == ' ' else False
        self.in_phrase = False

    def update_in_phrase(self, phrase):
        self.in_phrase = True if self.char in phrase else False

    def update_guess(self, guess):
        self.was_guessed = True if guess == self.char else False

    def show_char(self):
        return self.char if self.was_guessed else '_'
