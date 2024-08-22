#! /usr/bin/python3.12

from dataclasses import dataclass
from typing import Self

@dataclass
class Car:
  '''
  A class representing a Car
  '''
  # Fields
  car_brand: str
  car_fuel_type: str
  # Instance methods
  def drive(self: Self, distance: float) -> str:
    '''
    Indicates which brand of Car is used to travel the specified distance 
    '''
    return f"Driving '{self.car_brand}' running on '{self.car_fuel_type}' for a distance of '{distance}' km"