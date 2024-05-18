#! /usr/bin/python3.12

class SimpleObject:

  # Class attribute
  greet_name : str

  def __new__( klass , *args , **kwargs ):
    print( f'__new__() method' )
    return super().__new__(klass)
  
  # Initialize instance state
  def __init__( self , * , greet_name : str ) -> None:
    print( F'__init__() method' )
    self.greet_name = greet_name
    return None
  
  def say_hello( self , / ) -> None:
    print( f'Hello, {self.greet_name}!' )
    return None