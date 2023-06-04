from abc import ABC, abstractmethod
"""
This module defines the Game class and provides related functionality.
"""


class Game(ABC):
  """
    Represents a board game with title, current players, player limits, release_year, publisher.
    """
  default_game = None

  def __init__(self,
               title="",
               current_players=0,
               min_players=0,
               max_players=0,
               release_year=0,
               publisher="",
               game_themes=[]):
    self.title = title
    self.current_players = current_players
    self.min_players = min_players
    self.max_players = max_players
    self.release_year = release_year
    self.publisher = publisher
    self.game_themes = game_themes

  def __iter__(self):
    return iter(self.game_themes)

  def __getitem__(self, index):
    return list(self.game_themes)[index]

  @abstractmethod
  def connect_player(self):
    pass

  @abstractmethod
  def disconnect_player(self):
    pass

  def can_play(self):
    """
        Checks if the current number of players is within the allowed range.
        Returns True if the game can be played, False otherwise.
        """
    return self.min_players <= self.current_players <= self.max_players

  def __len__(self):
    return len(self.game_themes)

  def __str__(self):
    """
      Returns a string representation of the board game.
        """
    return f"Title: {self.title}, Current Players: {self.current_players}, Min Players: {self.min_players}, Max Players: {self.max_players}, Release Year: {self.release_year},Publisher: {self.publisher}"
