#! /usr/bin/python3.12

from dataclasses import dataclass

@dataclass(frozen=True,order=True)
class Comment:
  id: int
  text: str