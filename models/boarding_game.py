from models.game import Game
"""
This module defines the BoardingGame class and provides related functionality.
"""


class BoardingGame(Game):
  """
    Represents a boaring game with title, current players, player limits, release_year, publisher.
    """

  def __init__(self,
               title="",
               current_players=0,
               min_players=0,
               max_players=0,
               release_year=0,
               publisher="",
              game_themes=[]):
    super().__init__(title, current_players, min_players, max_players,
                   release_year, publisher,game_themes)

  @staticmethod
  def get_instance():
    """
        Returns the instance of the default board game.
        If the instance doesn't exist, creates a new one and returns it.
        """
    if not BoardingGame.default_game:
      BoardingGame.default_game = BoardingGame()
    return BoardingGame.default_game

  def __str__(self):
    """
      Returns a string representation of the boarding game.
        """
    return super().__str__()
