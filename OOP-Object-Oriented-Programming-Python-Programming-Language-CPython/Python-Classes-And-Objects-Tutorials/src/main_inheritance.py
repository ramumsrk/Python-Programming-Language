#! /usr/bin/python3.12

import logging

import logging_configuration
from python_oop_tutorial_object_oriented_programming_inheritance.cat.cat import Cat as Cat

# User-defined function
def main() -> None:
  '''
  Action happens here
  '''
  animal_cat: Cat = Cat(animal_name='Tim', animal_age=5, animal_color='Blue')
  logging.debug(f'{animal_cat=}')
  logging.debug(f'{animal_cat.__dict__=}')
  logging.debug(f'{animal_cat.speak()=}')
  return None

if __name__ == '__main__':
  logging.debug(f'Name of module is: {__name__}')
  logging.debug(f'File constituting module is: {__file__}')
  # Function call
  main()