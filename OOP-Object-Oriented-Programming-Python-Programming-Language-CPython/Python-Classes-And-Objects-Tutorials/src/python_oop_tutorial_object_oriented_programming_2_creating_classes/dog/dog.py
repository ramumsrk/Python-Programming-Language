#! /usr/bin/python3.12

from typing import Self, LiteralString, Tuple, Dict
import logging

class Dog:
  '''
  A class representing a Dog
  '''
  # Fields
  dog_name: str
  dog_age: int
  # Return an instance
  def __new__(klass: Self, *args: Tuple, **kwargs: Dict) -> Self:
    '''
    Return an instance
    '''
    return super().__new__(klass)
  # Instance initialization
  def __init__(self: Self, *, dog_name: str, dog_age: int) -> None:
    '''
    Instance initialization
    '''
    self.dog_name = dog_name
    self.dog_age = dog_age
    logging.debug(f'An instance of {self.__class__=} is being initialized')
    logging.debug(f'{self=}')
    logging.debug(f'{self.__dict__=}')
    return None
  # Instance method
  def speak(self: Self, /) -> LiteralString:
    '''
    Return the sound when a Dog instance barks
    '''
    return f'{self.dog_name=} aged {self.dog_age=} says woof!'