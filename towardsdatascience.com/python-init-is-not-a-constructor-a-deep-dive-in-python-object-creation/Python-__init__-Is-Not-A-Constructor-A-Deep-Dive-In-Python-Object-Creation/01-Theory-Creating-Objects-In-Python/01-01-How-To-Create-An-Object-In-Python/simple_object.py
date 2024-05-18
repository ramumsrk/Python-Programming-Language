#! /usr/bin/python3.12

class SimpleObject:

  # Class attribute
  greet_name : str

  def __init__( self , * , greet_name : str ) -> None:
    self.greet_name = greet_name
    return None
  
  def say_hello( self , / ) -> None:
    print( f'Hello, {self.greet_name}!' )
    return None