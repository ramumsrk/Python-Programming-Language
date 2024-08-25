#! /usr/bin/python3.12

import logging

import logging_configuration
from python_oop_tutorial_object_oriented_programming_2_creating_classes.dog.dog import Dog as Dog

# User-defined function
def main() -> None:
  # Create Dog instances
  tim: Dog = Dog(dog_name='Tim',dog_age=55)
  fred: Dog = Dog(dog_name='Fred',dog_age=3)
  # Details about 'tim'
  logging.debug(f'{type(tim)=}')
  logging.debug(f'{tim=}')
  # Details about 'fred'
  logging.debug(f'{type(fred)=}')
  logging.debug(f'{fred=}')
  # Invoking instance methods
  logging.debug(f'{tim.speak()=}')
  logging.debug(f'{fred.speak()=}')  
  return None

if __name__ == '__main__':
  logging.debug(f'Name of module is: {__name__}')
  logging.debug(f'File constituting module is: {__file__}')
  # Function call
  main()