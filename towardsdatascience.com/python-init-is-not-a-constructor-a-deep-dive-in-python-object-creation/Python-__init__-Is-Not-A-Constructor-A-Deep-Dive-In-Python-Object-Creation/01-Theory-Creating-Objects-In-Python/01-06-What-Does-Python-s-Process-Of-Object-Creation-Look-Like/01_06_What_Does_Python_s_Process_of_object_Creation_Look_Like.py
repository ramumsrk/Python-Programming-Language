#! /usr/bin/python3.12

from simple_object import SimpleObject

if __name__ == '__main__':

  first_simple_object : SimpleObject = SimpleObject(
    greet_name='Bob'
  )
  first_simple_object.say_hello()