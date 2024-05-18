#! /usr/bin/python3.12

class SimpleObject:

  # Class attribute
  greet_name : str

  def __new__( klass , *args , **kwargs ):
    print( f'Inside __new__()' )
    return super().__new__(klass)