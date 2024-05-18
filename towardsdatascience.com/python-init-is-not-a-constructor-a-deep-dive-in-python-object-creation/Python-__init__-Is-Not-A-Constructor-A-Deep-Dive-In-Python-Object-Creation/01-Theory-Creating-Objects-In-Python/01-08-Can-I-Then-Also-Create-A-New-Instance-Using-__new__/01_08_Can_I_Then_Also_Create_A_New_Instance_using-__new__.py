#! /usr/bin/python3.12

from simple_object import SimpleObject

if __name__ == '__main__':

  first_simple_object_instance : SimpleObject = SimpleObject(
    greet_name="First Instance"
  )
  first_simple_object_instance.say_hello()

  second_simple_object_instance : SimpleObject = SimpleObject.__new__(SimpleObject)
  second_simple_object_instance.__init__(
    greet_name="Second Instance"
  )
  second_simple_object_instance.say_hello()