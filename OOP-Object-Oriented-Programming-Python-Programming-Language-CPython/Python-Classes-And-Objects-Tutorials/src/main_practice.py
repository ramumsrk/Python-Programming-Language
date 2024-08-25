#! /usr/bin/python3.12

import logging

import logging_configuration
from practice_class_fields.practice.practice import Practice as Practice

# User-defined function
def main() -> None:
    first_practice: Practice = Practice(first_field=1, second_field="One")
    second_practice: Practice = Practice(first_field=2, second_field="Two")
    return None

if __name__ == '__main__':
    logging.debug(f'Name of module is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    # Function call
    main()