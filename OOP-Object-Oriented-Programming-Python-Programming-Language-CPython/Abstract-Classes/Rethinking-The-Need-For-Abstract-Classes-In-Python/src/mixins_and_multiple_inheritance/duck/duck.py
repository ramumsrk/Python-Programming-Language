#! /usr/bin/python3.12

from typing import Self, LiteralString

from mixins_and_multiple_inheritance.flymixin.flymixin import FlyMixin as FlyMixin

class Duck(FlyMixin):
  '''A class representing a FlyMixin'''
  def quack(self: Self) -> LiteralString:
    """A quck definition for a Duck instance"""
    return f'Quack! {self.__class__}'