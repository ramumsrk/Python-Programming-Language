#! /usr/bin/python3.12

import logging

from comment import Comment

from typing import Literal

from dataclasses import asdict

# User-defined function
def main() -> Literal[None]:
  # Logging configuration
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
  )
  first_comment : Comment = Comment(1, 'I just subscribed')
  logging.debug(F'{asdict(first_comment)}')
  return None

if __name__ == '__main__':
  # Function call
  main()