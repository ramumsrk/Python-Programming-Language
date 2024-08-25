#! /usr/bin/python3.12

import logging
from typing import Self, Tuple, Dict

import logging_configuration

from python_oop_tutorial_object_oriented_programming_inheritance.animal.animal import Animal as Animal

class Cat(Animal):
  '''
  A class representing a Cat
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
  def __init__(
    self: Self,
    *,
    animal_name: str,
    animal_age: int,
    animal_color: str  
  ) -> None:
    '''
    Initialize an instance state
    '''
    self.animal_name = animal_name
    self.animal_age = animal_age
    self.animal_color = animal_color
    logging.debug(f'{self=}')
    logging.debug(f'{self.__class__=}')
    logging.debug(f'{self.__dict__=}')
    return None
  def speak(self: Self, /) -> str:
    '''
    A cat instane starts to speak
    '''
    return f"'{self.animal_name=}', aged '{self.animal_age=}' years, and '{self.animal_color=}' coloured says meow!"