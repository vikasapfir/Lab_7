from gamemanager import GameManager
from models.cardgame import CardGame
from models.boardinggame import BoardingGame
from models.sportsgame import SportsGame
from models.computergame import ComputerGame
from sm import SM

game_manager = GameManager()


game_manager.add_game(CardGame.get_instance())
game_manager.add_game(CardGame.get_instance())
game_manager.add_game(CardGame("UNO", 3, 2, 15, 2002, "test", 1, 70))
game_manager.add_game(CardGame(release_year=1995))
game_manager.add_game(BoardingGame(release_year=2001))
game_manager.add_game(SportsGame(release_year=2005, has_referee=True))
game_manager.add_game(ComputerGame(release_year=2007, isMultiplayer=True))

game_manager.print_all_games()

    # Remove a game by index
game_manager.remove_by_index(1)

    # Find games with release year greater than 2010
games_with_release_year_greater_than_2010 = game_manager.find_games_with_release_year_greater_than(2010)
print("Games with release year greater than 2010:")
for game in games_with_release_year_greater_than_2010:
    print(game)

    # Get the length of the game_manager
length = len(game_manager)
print("Length of game_manager:", length)

    # Get the first game
first_game = game_manager[0]
print("First game:", first_game)

    # Iterate over games
print("Iterating over games:")
for game in game_manager:
    print(game)

def get_game_info(game):
    return f"Game (Release Year: {game.release_year}, Current Players: {game.current_players})"
    
common_results = game_manager.get_common_results(get_game_info)
print("Common results:")
for result in common_results:
    print(result)

    # Get concatenation with index
concatenation_with_index = game_manager.get_concatenation_with_index()
print("Concatenation with index:")
for item in concatenation_with_index:
    print(item)

    # Get zip results
zip_results = game_manager.get_zip_results(get_game_info)
print("Zip results:")
for result in zip_results:
    print(result)

    # Get attribute dictionary with value type 'int'
attribute_dict = game_manager.get_attribute_dictionary(int)
print("Attribute dictionary:")
for key, value in attribute_dict.items():
    print(f"{key}: {value}")

    # Check condition for all and any
def has_many_players(game):
    return game.current_players > 1

condition_results = game_manager.check_condition(has_many_players)
print("Condition results:")
print("All:", condition_results['all'])
print("Any:", condition_results['any'])
print("----------------------------\nРівень 2\n")

#Рівень 2
game_manager2 = GameManager([])

# Додавання декількох ігор до менеджера 
game1 = CardGame(title='Game 1', game_themes=['Theme 1', 'Theme 2', 'Theme 3'])
game2 = CardGame(title='Game 2', game_themes=['Theme 4', 'Theme 5'])
game3 = CardGame(title='Game 3', game_themes=['Theme 6', 'Theme 7', 'Theme 8'])

game_manager2.add_game(game1)
game_manager2.add_game(game2)
game_manager2.add_game(game3)

print(game_manager2.get_games())
# Створення об'єкту менеджера SM на основі менеджера 
sm = SM(game_manager2)

# Перевірка перевизначених методів
print(len(sm))  # Виведе 8
print("Четверта тематика: ",sm[3])   # Виведе 'Theme 4'
for theme in sm:
    print(theme)  # Виведе всі теми відповідно до порядку ітерації