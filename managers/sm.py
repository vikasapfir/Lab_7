"""
Module for Set Manager class.
"""

class SM:
    """
    Set Manager class.
    """

    def __init__(self, game_manager):
        self.game_manager = game_manager

    def __iter__(self):
        for game in self.game_manager.get_games():
            yield from game

    def __len__(self):
        return sum(len(game) for game in self.game_manager.get_games())

    def __getitem__(self, index):
        count = 0
        for game in self.game_manager.get_games():
            if count <= index < count + len(game):
                return game[index - count]
            count += len(game)
        raise IndexError('Index out of range')

    def __next__(self):
        for game in self.game_manager.get_games():
            for theme in game:
                yield theme

    def __str__(self):
        return 'Set Manager'
