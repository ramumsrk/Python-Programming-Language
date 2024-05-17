#! /usr/bin/python3.12

class Animal:
  def speak( self ) -> None:
    print( F"Animal {self.animal_name} sound" )
    return None
  def __init__( self , animal_name : str , / ) -> None:
    self.animal_name = animal_name
    return None