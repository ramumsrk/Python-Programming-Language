#! /usr/bin/python3.12

from typing import Self
from abc import ABC, abstractmethod

class Animal(ABC):
  '''
  A class representing an Animal
  '''
  # Attributes - Fields
  animal_name: str
  animal_age: int
  animal_color: str
  @abstractmethod
  def speak(self: Self, /) -> str:
    '''
    An animal instance starts to speak
    '''
    pass