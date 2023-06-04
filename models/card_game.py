from models.game import Game
"""
This module defines the CardGame class and provides related functionality.
"""


class CardGame(Game):
  """
    Represents a card game with number_of_decks, cards_per_deck, title, current players, player limits, release_year, publisher.
    """
  default_card_game = None

  def __init__(self,
               title="",
               current_players=0,
               min_players=0,
               max_players=0,
               release_year=0,
               publisher="",
               game_themes=[],
               number_of_decks=0,
               cards_per_deck=0):
    super().__init__(title, current_players, min_players, max_players,
                     release_year, publisher, game_themes)
    self.number_of_decks = number_of_decks
    self.cards_per_deck = cards_per_deck

  @staticmethod
  def get_instance():
    """
        Returns the instance of the default board game.
        If the instance doesn't exist, creates a new one and returns it.
        """
    if not CardGame.default_game:
      CardGame.default_game = CardGame()
    return CardGame.default_game


  def __str__(self):
    """
      Returns a string representation of the card game.
        """
    return super().__str__(
    ) + f",Number Of Decks: {self.number_of_decks}, Cards Per Deck: {self.cards_per_deck}"
