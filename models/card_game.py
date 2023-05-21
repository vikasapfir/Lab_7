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
               number_of_decks=0,
               cards_per_deck=0):
    super().__init__(title, current_players, min_players, max_players,
                   release_year, publisher)
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

  def connect_player(self):
    """
        Adds a player to the  game if the maximum number of players hasn't been reached.
        """
    if self.current_players < self.max_players:
      self.current_players += 1

  def disconnect_player(self):
    """
        Removes a player from the game if there is at least one player.
        """
    if self.current_players > 0:
      self.current_players -= 1

  def __str__(self):
    """
      Returns a string representation of the card game.
        """
    return super().__str__() + f",Number Of Decks: {self.number_of_decks}, Cards Per Deck: {self.cards_per_deck}"
