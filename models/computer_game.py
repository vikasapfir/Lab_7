from models.game import Game
"""
This module defines the ComputerGame class and provides related functionality.
"""


class ComputerGame(Game):
  """
    Represents a Computer game with title, current players, player limits, release_year, publisher.
    """

  def __init__(self,
               title="",
               current_players=0,
               min_players=0,
               max_players=0,
               release_year=0,
               publisher="",
               game_themes=[],
              isMultiplayer=False):
    super().__init__(title, current_players, min_players, max_players,
                   release_year, publisher,game_themes)
    self.isMultiplayer = isMultiplayer

  @staticmethod
  def get_instance():
    """
        Returns the instance of the default Computer game.
        If the instance doesn't exist, creates a new one and returns it.
        """
    if not ComputerGame.default_game:
      ComputerGame.default_game = ComputerGame()
    return ComputerGame.default_game

  def __str__(self):
    """
      Returns a string representation of the Computer game.
        """
    return super().__str__() + f",Is Multiplayer: {self.isMultiplayer}"
    
