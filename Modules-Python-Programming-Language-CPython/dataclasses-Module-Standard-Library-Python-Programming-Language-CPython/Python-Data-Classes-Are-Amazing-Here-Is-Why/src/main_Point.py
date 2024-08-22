#! /usr/bin/python3.12

import logging

import logging_configuration
from before_data_classes.point.point import Point as Point
import an_introduction_to_data_classes.point.point

# User-defined function
def main() -> None:
  first_point: Point = Point(x_coordinate=1, y_coordinate=2)
  second_point: Point = Point(x_coordinate=2, y_coordinate=1) 
  logging.debug(f'{first_point=}')
  logging.debug(f'{second_point=}')
  logging.debug(f'{(first_point == second_point)=}')
  third_point: an_introduction_to_data_classes.point.point.Point = an_introduction_to_data_classes.point.point.Point(x_coordinate=1, y_coordinate=2)
  fourth_point: an_introduction_to_data_classes.point.point.Point = an_introduction_to_data_classes.point.point.Point(x_coordinate=2, y_coordinate=1)
  logging.debug(f'{third_point=}')
  logging.debug(f'{fourth_point=}')
  logging.debug(f'{(third_point == fourth_point)=}')
  return None

if __name__ == '__main__':
  logging.debug(f'Name of module is: {__name__}')
  logging.debug(f'File containing module is: {__file__}')
  # Function call
  main()