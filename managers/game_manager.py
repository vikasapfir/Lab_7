class GameManager:

  def __init__(self, games=[]):
    self.games = games

  def add_game(self, game):
    self.games.append(game)

  def remove_game(self, game):
    self.games.remove(game)

  def remove_by_index(self, index):
    self.games.pop(index)

  def find_games_with_release_year_greater_than(self, release_year):
    return [game for game in self.games if game.release_year > release_year]

  def find_games_with_current_players_greater_than(self, current_players):
    return [
      game for game in self.games if game.current_players > current_players
    ]

  def get_games(self):
    return self.games

  def print_all_games(self):
    for game in self.games:
      print(game)

  def __len__(self):
    return len(self.games)

  def __getitem__(self, index):
    return self.games[index]

  def __iter__(self):
    return iter(self.games)

  def get_common_results(self, method):
    return [method(game) for game in self.games]

  def get_concatenation_with_index(self):
    return [f'{index}: {game}' for index, game in enumerate(self.games)]

  def get_zip_results(self, method):
    return [
      f'{game}: {result}'
      for game, result in zip(self.games, self.get_common_results(method))
    ]

  #формуємо словник з атрибутів
  def get_attribute_dictionary(self, value_type):
    return {
      attr: getattr(game, attr)
      for game in self.games for attr in vars(game) if
      not attr.startswith('__') and isinstance(getattr(game, attr), value_type)
    }

  def check_condition(self, condition):
    return {
      'all': all(condition(game) for game in self.games),
      'any': any(condition(game) for game in self.games)
    }
