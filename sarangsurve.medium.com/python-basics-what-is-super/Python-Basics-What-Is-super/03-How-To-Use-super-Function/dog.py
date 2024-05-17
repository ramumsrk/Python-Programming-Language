#! /usr/bin/python3.12

import logging

from animal import Animal

class Dog( Animal ):
  def speak( self ) -> None:
    super().speak()
    print( f"{self.dog_name} says Woof!" )
    return None
  def __init__( self , dog_name : str , / ) -> None:
    super().__init__(dog_name)
    self.dog_name = dog_name
    return None