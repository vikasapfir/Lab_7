from models.game import Game
"""
This module defines the SportsGame class and provides related functionality.
"""


class SportsGame(Game):
  """
    Represents a sports game with title, current players, player limits, release_year, publisher.
    """

  def __init__(self,
               title="",
               current_players=0,
               min_players=0,
               max_players=0,
               release_year=0,
               publisher="",
               game_themes=[],
               has_referee=False):
    super().__init__(title, current_players, min_players, max_players,
                     release_year, publisher,game_themes)
    self.has_referee = has_referee

  @staticmethod
  def get_instance():
    """
        Returns the instance of the default Sports game.
        If the instance doesn't exist, creates a new one and returns it.
        """
    if not SportsGame.default_game:
      SportsGame.default_game = SportsGame()
    return SportsGame.default_game


  def __str__(self):
    """
      Returns a string representation of the sports game.
        """
    return super().__str__() + f",Has Referee: {self.has_referee}"
