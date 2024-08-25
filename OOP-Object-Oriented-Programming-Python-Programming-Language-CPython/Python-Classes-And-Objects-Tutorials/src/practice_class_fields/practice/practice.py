#! /usr/bin/python3.12

import logging
from typing import Self, Dict, Tuple

class Practice:
    # Attributes - Fields
    first_field: int
    second_field: str
    # Attributes - Methods
    def __new__(cls: Self, *args: Tuple, **kwargs: Dict) -> Self:
        """
        Create a new instance of the Practice class.
        """
        return super().__new__(cls)
    def __init__(self: Self, *, first_field: int, second_field: str) -> None:
        """
        Initialize a new instance of the Practice class.
        """
        self.first_field = first_field
        self.second_field = second_field
        logging.debug(f'{self=}')
        logging.debug(f'{self.__class__=}')
        logging.debug(f'{self.__dict__=}')
        return None