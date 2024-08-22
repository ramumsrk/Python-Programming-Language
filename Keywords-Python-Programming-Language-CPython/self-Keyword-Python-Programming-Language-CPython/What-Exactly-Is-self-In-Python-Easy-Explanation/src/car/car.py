#! /usr/bin/python3.12

from typing import Self

class Car:
  '''
  A class representing a Car
  '''
  # Fields
  car_brand: str
  car_fuel_type: str
  # Instance initialization
  def __init__(
    self: Self,
    car_brand: str,
    car_fuel_type: str  
  ) -> None:
    '''
    Initialize a Car instance
    '''
    self.car_brand = car_brand
    self.car_fuel_type = car_fuel_type
    return None