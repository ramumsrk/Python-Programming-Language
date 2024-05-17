#! /usr/bin/python3.12

class Parent:
  def __init__( self , * , attribute_name : str ) -> None:
    self.attribute_name = attribute_name
    return None
  def print_attributes( self ) -> None:
    print( f'Attribute name: {self.attribute_name}' )
    return None