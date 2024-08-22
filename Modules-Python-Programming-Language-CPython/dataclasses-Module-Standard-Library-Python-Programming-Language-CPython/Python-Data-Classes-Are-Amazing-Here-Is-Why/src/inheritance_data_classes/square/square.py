#! /usr/bin/python3.12

from dataclasses import dataclass
from typing import Self

from inheritance_data_classes.rectangle.rectangle import Rectangle as Rectangle

@dataclass
class Square(Rectangle):
  '''
  A class representing a Square
  '''
  side_of_a_square: int
  def __post__init__(self: Self) -> Self:
    '''
    Initialize super class instance state
    '''
    return super().__init__(self.side_of_a_square, self.side_of_a_square)