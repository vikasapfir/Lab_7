class TooMuchPlayersException(Exception):
  def __init__(self,message="Too much players in the game!"):
      self.message = message
      super().__init__(self.message)

class NegativeNumberOfPlayersException(Exception):
  def __init__(self,message="Number of players can't be less than 0!"):
      self.message = message
      super().__init__(self.message)
    