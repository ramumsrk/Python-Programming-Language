#! /usr/bin/python3.12

from comment import Comment

from inspect import getmembers , isfunction

import logging

from typing import Literal

from pprint import pprint

# User-defined function
def main() -> Literal[None]:
  # Loggin configuration
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%s %H:%M:%S"
  )
  logging.debug(f'{getmembers(Comment,isfunction)}')
  pprint(getmembers(Comment,isfunction))
  return None

if __name__ == '__main__':
  # Function call
  main()