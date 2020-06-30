from phrasehunter.game import Game


PHRASES = [
    'cat in the hat',
    'fox in the box',
    'dog in the fog',
    'bird is the word',
    'snake in the lake',
    'too bad you got this phrase',
]

if __name__ == '__main__':
    game = Game(PHRASES)
    game.start_game()
