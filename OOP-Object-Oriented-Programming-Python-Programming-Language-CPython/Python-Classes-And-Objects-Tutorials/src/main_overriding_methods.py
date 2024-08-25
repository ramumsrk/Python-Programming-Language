#! /usr/bin/python3.12

import logging

import logging_configuration
from python_oop_tutorial_object_oriented_programming_overriding_methods.point.point import Point as Point

# User-defined function
def main() -> None:
    """
    Action happens here
    """
    first_point: Point = Point(x_coordinate=3,y_coordinate=4)
    second_point: Point = Point(x_coordinate=3,y_coordinate=2)
    third_point: Point = Point(x_coordinate=1,y_coordinate=3)
    fourth_point: Point = Point(x_coordinate=0,y_coordinate=1)
    fifth_point: Point = first_point + second_point
    logging.debug(f'{fifth_point=}')
    logging.debug(f'{fifth_point.__class__=}')
    logging.debug(f'{fifth_point.__dict__=}')
    return None

if __name__ == '__main__':
    logging.debug(f'Name of module is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    # Function call
    main()