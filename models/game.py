from abc import ABC, abstractmethod
from exceptions import TooMuchPlayersException
from exceptions import NegativeNumberOfPlayersException
from decorator import logged

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

  @logged(TooMuchPlayersException,"file")
  def connect_player(self):
    """
        Adds a player to the  game if the maximum number of players hasn't been reached.
        """
    if self.current_players < self.max_players:
      self.current_players += 1
    else:
      raise TooMuchPlayersException()

  @logged(NegativeNumberOfPlayersException,"file")
  def disconnect_player(self):
    """
        Removes a player from the game if there is at least one player.
        """
    if self.current_players > 0:
      self.current_players -= 1
    else:
      raise  NegativeNumberOfPlayersException()


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
