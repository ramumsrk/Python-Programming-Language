#! /usr/bin/python3.12

from typing import Self, LiteralString, Literal

class Point:
  '''
  A class representing a two-dimensional Point
  '''
  x_coordinate: int
  y_coordinate: int
  # Initialize instance state
  def __init__(self: Self, x_coordinate: int, y_coordinate: int) -> None:
    '''
    Initialize a Point instance
    '''
    self.x_coordinate = x_coordinate
    self.y_coordinate = y_coordinate
    return None
  # Internal representation of a Point instance
  def __repr__(self: Self, /) -> LiteralString:
    '''
    Internal representation of a Point instance
    '''
    return f'Point(x={self.x_coordinate}, y={self.y_coordinate})'
  # Check equality of two Point instances
  def __eq__(self: Self, point: Self.__class__) -> Literal[True,False]:
    '''
    Check equality of two Point instances
    '''
    return True if self.x_coordinate == point.x_coordinate and self.y_coordinate == point.y_coordinate else False