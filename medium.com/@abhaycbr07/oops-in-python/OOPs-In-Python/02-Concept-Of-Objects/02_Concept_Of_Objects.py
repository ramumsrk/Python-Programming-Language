#! /usr/bin/python3.12

from car import Car

if __name__ == '__main__':

  toyota_car : Car = Car(
    car_make="Toyota",
    car_model="Camry",
    car_year=2022
  )
  toyota_car.print_car_information()

  honda_car : Car = Car(
    car_make="Honda",
    car_model="Accord",
    car_year=2021
  )
  honda_car.print_car_information()