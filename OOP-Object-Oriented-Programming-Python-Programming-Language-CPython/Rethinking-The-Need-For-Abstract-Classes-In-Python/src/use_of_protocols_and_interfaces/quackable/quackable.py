#! /usr/bin/python3.12

from typing import Protocol, Self, LiteralString

class Quackable(Protocol):
  """A class representing a Quackable being"""
  def quack(self: Self) -> LiteralString:
    '''Quack behaviour definition'''
    return f'{self.__class__}'
    