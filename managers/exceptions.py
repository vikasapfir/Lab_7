"""
Exceptions module for game-related exceptions.
"""


class TooMuchPlayersException(Exception):
    """Exception raised when there are too many players in the game."""

    def __init__(self, message="Too much players in the game!"):
        self.message = message
        super().__init__(self.message)


class NegativeNumberOfPlayersException(Exception):
    """Exception raised when the number of players is less than 0."""

    def __init__(self, message="Number of players can't be less than 0!"):
        self.message = message
        super().__init__(self.message)
