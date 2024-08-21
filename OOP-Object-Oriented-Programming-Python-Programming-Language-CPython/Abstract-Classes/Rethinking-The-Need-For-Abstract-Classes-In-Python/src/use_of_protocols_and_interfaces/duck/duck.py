#! /usr/bin/python3.12

from typing import Self, LiteralString

class Duck:
  """A class representing a Duck"""
  def quack(self: Self, /) -> LiteralString:
    '''Quack definition for a Duck instance'''
    return f'Quack!'