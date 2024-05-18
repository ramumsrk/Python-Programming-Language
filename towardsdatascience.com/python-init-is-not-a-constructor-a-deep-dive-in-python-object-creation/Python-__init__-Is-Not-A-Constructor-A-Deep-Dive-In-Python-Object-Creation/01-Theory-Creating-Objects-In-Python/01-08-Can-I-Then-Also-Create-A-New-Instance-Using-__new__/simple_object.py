#! /usr/bin/python3.12

class SimpleObject:

  # Class attribute
  greet_name : str

  # Allocate memory and return reference
  # Override __new__
  def __new__( klass , *args , **kwargs ):
    print( f'Inside __new__()' )
    return super().__new__(klass)
  
  # Initialize instance state
  def __init__( self , * , greet_name : str ) -> None:
    print( F'Inside __init__()' )
    self.greet_name = greet_name
    return None
  
  def say_hello( self , / ) -> None:
    print( F'Hello, {self.greet_name}!' )
    return None