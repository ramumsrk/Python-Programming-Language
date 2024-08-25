#! /usr/bin/python3.12

from typing import Self, LiteralString, Tuple, Dict
import logging

import logging_configuration
from python_oop_tutorial_object_oriented_programming_inheritance.animal.animal import Animal as Animal

class Dog(Animal):
  '''
  A class representing a Dog
  '''
  # Attributes - Methods
  def __new__(
    klass: Self,
    *args: Tuple,
    **kwargs: Dict
  ) -> Self:
    '''
    Create and return an instance
    '''
    return super().__new__(klass)
  # Instance initialization
  def __init__(
    self: Self,
    *,
    dog_name: str,
    dog_age: int,
    dog_color: str
  ) -> None:
    '''
    Instance initialization
    '''
    self.animal_name = dog_name
    self.animal_age = dog_age
    self.animal_color = dog_color 
    logging.debug(f'{self=}')
    logging.debug(f'{self.__class__=}')
    logging.debug(f'{self.__dict__=}')
    return None
  # Instance method
  def speak(self: Self, /) -> LiteralString:
    '''
    Return the sound when a Dog instance barks
    '''
    return f"'{self.animal_name=}' aged '{self.animal_age=}' years, and coloured '{self.animal_color=}' says woof!"