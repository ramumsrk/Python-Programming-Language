#! /usr/bin/python3.12

import logging

logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S"
)

# User-defined function
def numbers_divisible_by_three( input_number : int ) -> None:
  for sample_input_number in range(input_number):
    if sample_input_number % 3 == 0:
      logging.debug(
        f'Number: {sample_input_number}'
      )
  return None

if __name__ == '__main__':

  logging.debug(
    F'{numbers_divisible_by_three(14)}'
  )