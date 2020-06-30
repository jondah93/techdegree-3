from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase):
        self.original_phrase = phrase
        self.phrase_chars = []
        for char in phrase.strip():
            char = Character(char)
            char.update_in_phrase(phrase)
            self.phrase_chars.append(char)

    def print_phrase(self):
        output = ''
        for char in self.phrase_chars:
            output += char.show_char()
        return output

    def phrase_guessed(self):
        return True if self.print_phrase().lower() == self.original_phrase.lower() else False

    def __iter__(self):
        yield from self.phrase_chars
