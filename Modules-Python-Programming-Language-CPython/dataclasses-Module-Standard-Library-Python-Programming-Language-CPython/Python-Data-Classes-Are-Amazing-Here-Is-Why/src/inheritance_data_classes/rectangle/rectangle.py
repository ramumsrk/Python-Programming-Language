#! /usr/bin/python3.12

from typing import Self

class Rectangle:
  '''
  A class representing a Rectangle
  '''
  # Fields
  height: int
  width: int
  # Instance initialization
  def __init__(
    self: Self,
    height: int,
    width: int  
  ) -> None:
    '''
    Instance initial state
    '''
    self.height = height
    self.width = width
    return None