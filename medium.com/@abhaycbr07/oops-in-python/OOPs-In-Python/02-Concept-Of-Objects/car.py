#! /usr/bin/python3.12

class Car:
  def __init__( self , * , car_make : str , car_model : str , car_year : int ) -> None:
    self.car_make = car_make
    self.car_model = car_model
    self.car_year = car_year
    return None
  def print_car_information( self , / ) -> None:
    print( f'Car make: {self.car_make}\nCar model: {self.car_model}\nCar manufacturing year: {self.car_year}' )