"""
This module contains the GameManager class for managing games.
"""

class GameManager:
    """
    A class for managing games.
    """

    def __init__(self):
        """
        Initialize an instance of GameManager.
        """
        self.games = []

    def __len__(self):
        """
        Get the length of the game list.

        Returns:
            int: The number of games in the list.
        """
        return len(self.games)

    def __getitem__(self, index):
        """
        Get a game from the list by index.

        Args:
            index (int): The index of the game to retrieve.

        Returns:
            object: The game at the specified index.
        """
        return self.games[index]

    def __iter__(self):
        """
        Make the GameManager iterable.

        Returns:
            object: An iterator over the games list.
        """
        return iter(self.games)

    def add_game(self, game):
        """
        Add a game to the list of games.

        Args:
            game (object): The game object to add.
        """
        self.games.append(game)

    def remove_game(self, game):
        """
        Remove a game from the list of games.

        Args:
            game (object): The game object to remove.
        """
        self.games.remove(game)

    def remove_by_index(self, index):
        """
        Remove a game at the specified index from the list of games.

        Args:
            index (int): The index of the game to remove.
        """
        self.games.pop(index)

    def find_games_with_release_year_greater_than(self, release_year):
        """
        Find games with a release year greater than the specified year.

        Args:
            release_year (int): The release year to compare.

        Returns:
            list: A list of games with a release year greater than `release_year`.
        """
        return [game for game in self.games if game.release_year > release_year]

    def find_games_with_current_players_greater_than(self, current_players):
        """
        Find games with the current number of players greater than the specified number.

        Args:
            current_players (int): The number of players to compare.

        Returns:
            list: A list of games with a current number of players greater than `current_players`.
        """
        return [game for game in self.games if game.current_players > current_players]

    def get_games(self):
        """
        Get the list of games.

        Returns:
            list: The list of games.
        """
        return self.games

    def print_all_games(self):
        """
        Print all games in the list.
        """
        for game in self.games:
            print(game)

    def get_method_results(self, method_name):
        """
        Get the results of executing a method for each game in the list.

        Args:
            method_name (str): The name of the method to execute.

        Returns:
            list: A list of results from executing the specified method for each game.
        """
        return [getattr(game, method_name)() for game in self.games]

    def get_game_with_index(self):
        """
        Get a tuple of game objects and their corresponding indices in the list.

        Returns:
            list: A list of tuples containing the index and game object for each game.
        """
        return [(index, game) for index, game in enumerate(self.games)]

    def get_game_and_method_result(self, method_name):
        """
        Get a tuple of game objects and the result of executing a method for each game.

        Args:
            method_name (str): The name of the method to execute.

        Returns:
            list: A list of tuples containing the game object and the result of executing the method for each game.
        """
        return [(game, getattr(game, method_name)()) for game in self.games]

    def get_attributes_by_type(self, attr_type):
        """
        Get a dictionary of attributes and their values for each game, filtered by the specified attribute type.

        Args:
            attr_type (type): The type of attribute values to include in the dictionary.

        Returns:
            dict: A dictionary mapping attribute names to their corresponding values for each game.
        """
        return {
            key: value
            for game in self.games
            for key, value in game.__dict__.items()
            if isinstance(value, attr_type)
        }

    def check_condition(self, condition):
        """
        Check if all or any games in the list satisfy the specified condition.

        Args:
            condition (function): A function that takes a game object and returns a boolean value.

        Returns:
            dict: A dictionary with keys "all" and "any" indicating whether all or any games satisfy the condition,
                respectively.
        """
        return {
            "all": all(condition(game) for game in self.games),
            "any": any(condition(game) for game in self.games),
        }
