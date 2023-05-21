
class GameManager:


  games = []


  
  def add_game(self,game):
    self.games.append(game)

  def remove_game(self,game):
    self.games.remove(game)

  def remove_by_index(self,index):
    self.games.pop(index)

  def find_games_with_release_year_greater_than(self, release_year):

    return [game for game in self.games if game.release_year > release_year]


  def find_games_with_current_players_greater_than(self, current_players):
    return [game for game in self.games if game.current_players > current_players]

  def get_games(self):
    return self.games
  
  def print_all_games(self):
    for game in self.games:
      print(game)



  
  