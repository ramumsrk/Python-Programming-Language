#! /usr/bin/python3.12

import logging

import logging_configuration
from dataclasses_car.car import Car as Car

# User-defined function
def main() -> None:
  volvo: Car = Car(car_brand='Volvo', car_fuel_type='Diesel')
  logging.debug(f'{volvo=}')
  logging.debug(f'{volvo.drive(distance=10)=}')
  bmw: Car = Car(car_brand='BMW', car_fuel_type='Electric')
  logging.debug(f'{bmw=}')
  logging.debug(f'{bmw.drive(distance=10)=}')  
  return None

if __name__ == '__main__':
  logging.debug(f'Name of module is: {__name__}')
  logging.debug(f'File constituting module is: {__file__}')
  # Function call
  main()