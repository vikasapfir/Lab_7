from gamemanager import GameManager
from models.cardgame import CardGame
from models.boardinggame import BoardingGame
from models.sportsgame import SportsGame
from models.computergame import ComputerGame
from sm import SM



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
