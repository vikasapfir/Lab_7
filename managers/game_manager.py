"""
Module representing a game manager.
"""
class GameManager:
    """
    Class representing a game manager.
    """

    def __init__(self, games=None):
        """
        Initialize a GameManager instance.

        Args:
            games (list, optional): List of games. Defaults to None.
        """
        self.games = games or []

    def add_game(self, game):
        """
        Add a game to the game manager.

        Args:
            game: Game object to be added.
        """
        self.games.append(game)

    def remove_game(self, game):
        """
        Remove a game from the game manager.

        Args:
            game: Game object to be removed.
        """
        self.games.remove(game)

    def remove_by_index(self, index):
        """
        Remove a game from the game manager by index.

        Args:
            index (int): Index of the game to be removed.
        """
        self.games.pop(index)

    def find_games_with_release_year_greater_than(self, release_year):
        """
        Find games with a release year greater than the given value.

        Args:
            release_year (int): Release year threshold.

        Returns:
            list: List of games with release year greater than the threshold.
        """
        return [game for game in self.games if game.release_year > release_year]

    def find_games_with_current_players_greater_than(self, current_players):
        """
        Find games with the number of current players greater than the given value.

        Args:
            current_players (int): Current players threshold.

        Returns:
            list: List of games with current players greater than the threshold.
        """
        return [game for game in self.games if game.current_players > current_players]

    def get_games(self):
        """
        Get the list of games.

        Returns:
            list: List of games.
        """
        return self.games

    def print_all_games(self):
        """
        Print all games in the game manager.
        """
        for game in self.games:
            print(game)

    def __len__(self):
        """
        Get the number of games in the game manager.

        Returns:
            int: Number of games.
        """
        return len(self.games)

    def __getitem__(self, index):
        """
        Get a game from the game manager by index.

        Args:
            index (int): Index of the game.

        Returns:
            Game: Game object.
        """
        return self.games[index]

    def __iter__(self):
        """
        Iterate over the games in the game manager.

        Returns:
            iter: Iterator object.
        """
        return iter(self.games)

    def get_common_results(self, method):
        """
        Get the common results of a method for all games.

        Args:
            method: Method to be applied to each game.

        Returns:
            list: List of results.
        """
        return [method(game) for game in self.games]

    def get_concatenation_with_index(self):
        """
        Get the concatenation of game strings with their index.

        Returns:
            list: List of strings with index.
        """
        return [f'{index}: {game}' for index, game in enumerate(self.games)]

    def get_zip_results(self, method):
        """
        Get the zipped results of a method applied to each game.

        Args:
            method: Method to be applied to each game.

        Returns:
            list: List of strings with game and result.
        """
        return [f'{game}: {result}' for game, result in zip(self.games, \
self.get_common_results(method))]

    def get_attribute_dictionary(self, value_type):
        """
        Get a dictionary of game attributes filtered by value type.

        Args:
            value_type (type): Value type to filter attributes.

        Returns:
            dict: Dictionary of attributes and their values.
        """
        return {
            attr: getattr(game, attr)
            for game in self.games
            for attr in vars(game)
            if not attr.startswith('__') and isinstance(getattr(game, attr), value_type)
        }

    def check_condition(self, condition):
        """
        Check if the given condition is satisfied for all or any games.

        Args:
            condition (function): Condition function that takes a game object.

        Returns:
            dict: Dictionary indicating if the condition is satisfied for all and any games.
        """
        return {
            'all': all(condition(game) for game in self.games),
            'any': any(condition(game) for game in self.games)
        }
