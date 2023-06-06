"""
This module defines the Game class and provides related functionality.
"""

from abc import ABC, abstractmethod

class Game(ABC):
    """
    Represents a board game with title, current players, player limits, release_year, publisher.
    """

    default_game = None

    def __init__(self, title="", current_players=0, min_players=0, max_players=0, \
release_year=0, publisher=""):
        self.title = title
        self.current_players = current_players
        self.min_players = min_players
        self.max_players = max_players
        self.release_year = release_year
        self.publisher = publisher

    @abstractmethod
    def connect_player(self):
        """
        Abstract method to connect a player to the game.
        """

    @abstractmethod
    def disconnect_player(self):
        """
        Abstract method to disconnect a player from the game.
        """
    def can_play(self):
        """
        Checks if the current number of players is within the allowed range.
        Returns True if the game can be played, False otherwise.
        """
        return self.min_players <= self.current_players <= self.max_players

    def __str__(self):
        """
        Returns a string representation of the board game.
        """
        return f"Title: {self.title}, Current Players: {self.current_players}, \
Min Players: {self.min_players}, Max Players: {self.max_players}, \
Release Year: {self.release_year}, Publisher: {self.publisher}"