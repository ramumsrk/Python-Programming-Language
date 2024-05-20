#! /usr/bin/python3.12

import logging

# User-defined function
def factorial( input_number : int , / ) -> int:
  if input_number <= 1:
    return 1
  else:
    return input_number * factorial( input_number - 1 )

if __name__ == '__main__':

  # Logging configuration
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
  )

  logging.debug(
    f'{factorial(4)}'
  )