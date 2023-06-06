"""
Main module for game management.
"""

from models.card_game import CardGame

game = CardGame("UNO", 3, 2, 4, 2002, "test", 1, 70)

game.connect_player()
game.connect_player()
game.connect_player()
game.connect_player()
game.disconnect_player()
game.disconnect_player()
game.disconnect_player()
game.disconnect_player()
game.disconnect_player()
game.disconnect_player()
game.disconnect_player()
