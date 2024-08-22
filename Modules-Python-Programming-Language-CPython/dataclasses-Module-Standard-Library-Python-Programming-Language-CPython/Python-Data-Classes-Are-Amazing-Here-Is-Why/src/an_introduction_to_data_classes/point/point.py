#! /usr/bin/python3.12

from dataclasses import dataclass

@dataclass
class Point:
  '''
  A class representing a Point
  '''
  x_coordinate: int
  y_coordinate: int