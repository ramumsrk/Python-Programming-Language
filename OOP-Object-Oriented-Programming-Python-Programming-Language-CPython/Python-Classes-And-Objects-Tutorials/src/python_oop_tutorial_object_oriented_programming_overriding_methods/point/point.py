#! /usr/bin/python3.12

from typing import Self, Tuple, Dict
import logging

class Point:
    """
    A class representing a point.
    """
    # Attributes - Fields
    x_coordinate: int
    y_coordinate: int
    # Attributes - Methods
    def __new__(cls: Self, *args: Tuple, **kwargs: Dict) -> Self:
        """
        Create a new instance of Point.
        """
        return super().__new__(cls)
    def __init__(self: Self, *, x_coordinate: int, y_coordinate: int) -> None:
        """
        Initialize a new instance of Point.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        logging.debug(f'{self=}')
        logging.debug(f'{self.__class__=}')
        logging.debug(f'{self.__dict__=}')
        return None
    def __add__(self: Self, point: Self) -> Self:
        """
        Add two points together.
        """
        self.x_coordinate += point.x_coordinate
        self.y_coordinate += point.y_coordinate
        return Point(x_coordinate=self.x_coordinate, y_coordinate=self.y_coordinate)
