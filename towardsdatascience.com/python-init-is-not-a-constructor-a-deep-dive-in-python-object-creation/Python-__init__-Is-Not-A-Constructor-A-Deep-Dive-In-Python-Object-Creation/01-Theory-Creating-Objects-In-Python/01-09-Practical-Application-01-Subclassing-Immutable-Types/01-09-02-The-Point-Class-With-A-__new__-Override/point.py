#! /usr/bin/python3.12

class Point(tuple):

  # Class attributes
  x_coordinate : float
  y_coordinate : float

  # Initialize instance state
  def __init__( self , * , x_coordinate : float , y_coordinate : float ) -> None:
    self.x_coordinate = x_coordinate
    self.y_coordinate = y_coordinate
    return None