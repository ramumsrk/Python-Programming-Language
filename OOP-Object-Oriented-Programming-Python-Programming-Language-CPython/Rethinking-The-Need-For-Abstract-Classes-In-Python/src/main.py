#! /usr/bin/python3.12

import logging

import logging_configuration
from use_of_protocols_and_interfaces.duck.duck import Duck as Duck
from use_of_protocols_and_interfaces.quackable.quackable import Quackable as Quackable

# User-defined function
def make_quack(duck: Quackable) -> None:
  logging.debug(f'{duck.quack()=}')
  return None

# User-defined function
def main() -> None:
  duck: Duck = Duck()
  logging.debug(f'{duck.quack()=}')
  logging.debug(f'{make_quack(duck)=}')
  return None

if __name__ == '__main__':
  logging.debug(f'Name of module: {__name__}')
  logging.debug(f'File containing module is: {__file__}')
  # Function call
  main()