"""
This module defines the BoardGame class and provides related functionality.
"""
class BoardGame:
    """
    Represents a board game with title, current players, and player limits.
    """
    default_board_game = None

    def __init__(self, title="", current_players=0, min_players=0, max_players=0):
        self.title = title
        self.current_players = current_players
        self.min_players = min_players
        self.max_players = max_players

    @staticmethod
    def get_instance():
        """
        Returns the instance of the default board game.
        If the instance doesn't exist, creates a new one and returns it.
        """
        if not BoardGame.default_board_game:
            BoardGame.default_board_game = BoardGame()
        return BoardGame.default_board_game

    def add_player(self):
        """
        Adds a player to the board game if the maximum number of players hasn't been reached.
        """
        if self.current_players < self.max_players:
            self.current_players += 1

    def remove_player(self):
        """
        Removes a player from the board game if there is at least one player.
        """
        if self.current_players > 0:
            self.current_players -= 1

    def can_play(self):
        """
        Checks if the current number of players is within the allowed range.
        Returns True if the game can be played, False otherwise.
        """
        return self.min_players <= self.current_players <= self.max_players

    def __str__(self):
        """
        Returns a string representation of the board game.
        """
        return f"Title: {self.title}, Current Players: {self.current_players}\
, Min Players: {self.min_players}, Max Players: {self.max_players}"

games = [
    BoardGame(),
    BoardGame("UNO", 3, 2, 15),
    BoardGame.get_instance(),
    BoardGame.get_instance(),
]

for game in games:
    print(game)
    
  