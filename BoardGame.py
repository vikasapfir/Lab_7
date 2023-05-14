class BoardGame:
    default_board_game = None

    def __init__(self, title="", current_players=0, min_players=0, max_players=0):
        self.title = title
        self.current_players = current_players
        self.min_players = min_players
        self.max_players = max_players

    def get_instance():
        if not BoardGame.default_board_game:
            BoardGame.default_board_game = BoardGame()
        return BoardGame.default_board_game

    def add_player(self):
        if self.current_players < self.max_players:
            self.current_players += 1

    def remove_player(self):
        if self.current_players > 0:
            self.current_players -= 1

    def can_play(self):
        return self.min_players <= self.current_players <= self.max_players

    def __str__(self):
        return f"Title: {self.title}, Current Players: {self.current_players}, Min Players: {self.min_players}, Max Players: {self.max_players}"

games = [
    BoardGame(),
    BoardGame("UNO", 3, 2, 15),
    BoardGame.get_instance(),
    BoardGame.get_instance(),
]

for game in games:
    print(game)
    
    
