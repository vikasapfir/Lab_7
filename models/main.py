from game_manager import GameManager
from models.card_game import CardGame
from models.boarding_game import BoardingGame
from models.sports_game import SportsGame
from models.computer_game import ComputerGame

game_manager = GameManager()


game_manager.add_game(CardGame.get_instance())
game_manager.add_game(CardGame.get_instance())
game_manager.add_game(CardGame("UNO", 3, 2, 15, 2002, "test", 1, 70))
game_manager.add_game(CardGame(release_year=1995))
game_manager.add_game(BoardingGame(release_year=2001))
game_manager.add_game(SportsGame(release_year=2005, has_referee=True))
game_manager.add_game(ComputerGame(release_year=2007, isMultiplayer=True))

game_manager.print_all_games()

print("\nAll games with release year greater than 2000: ")

for game in game_manager.find_games_with_release_year_greater_than(2000):
  print(game)


