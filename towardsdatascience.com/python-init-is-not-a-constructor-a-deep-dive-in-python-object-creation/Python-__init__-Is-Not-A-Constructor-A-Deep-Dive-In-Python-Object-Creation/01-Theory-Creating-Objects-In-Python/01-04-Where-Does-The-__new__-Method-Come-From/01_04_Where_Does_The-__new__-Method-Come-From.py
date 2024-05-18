#! /usr/bin/python3.12

from simple_object import SimpleObject

if __name__ == '__main__':

  first_simple_object : SimpleObject = SimpleObject(
    greet_name='Bob'
  )

  print( f'Is {first_simple_object} an instance of {object}? {isinstance(first_simple_object,object)}' )

  print( f'Is {42} an instance of {object}? {isinstance(42,object)}' )

  print( f'Is {"hello world"} an instance of {object}? {isinstance("hello world",object)}' )

  print( f'Is {{}} an instance of {object}? {isinstance({},object)}' )