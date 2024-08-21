#! /usr/bin/python3.12

from typing import Self, LiteralString

class FlyMixin:
  """A class representing a FlyMixin"""
  def fly(self: Self, /) -> LiteralString:
    return f'I can fly!'