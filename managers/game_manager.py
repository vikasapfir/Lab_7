"""
This module contains the GameManager class for managing games.
"""

class GameManager:
    """
    A class for managing games.
    """
    games = []

    def add_game(self, game):
        """Add a game to the list of games."""
        self.games.append(game)

    def remove_game(self, game):
        """Remove a game from the list of games."""
        self.games.remove(game)

    def remove_by_index(self, index):
        """Remove a game at the specified index from the list of games."""
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
        """Print all games in the list."""
        for game in self.games:
            print(game)
