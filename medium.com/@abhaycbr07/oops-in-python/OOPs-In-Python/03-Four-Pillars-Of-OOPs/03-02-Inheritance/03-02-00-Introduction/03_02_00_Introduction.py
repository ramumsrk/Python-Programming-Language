#! /usr/bin/python3.12

from child import Child

if __name__ == '__main__':

  first_child : Child = Child(
    attribute_name='Abhay',
    attribute_age=22
  )
  first_child.print_attributes()