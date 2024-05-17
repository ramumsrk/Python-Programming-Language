#! /usr/bin/python3.12

from parent import Parent

class Child(Parent):
  def __init__( self , * , attribute_name : str , attribute_age : int ) -> None:
    super().__init__(attribute_name=attribute_name)
    self.attribute_name = attribute_name
    self.attribute_age = attribute_age
    return None
  def print_attributes( self ) -> None:
    super().print_attributes()
    print( F'Attribute name: {self.attribute_name}\nAttribute age: {self.attribute_age}' )
    return None