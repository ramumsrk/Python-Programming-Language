#! /usr/bin/python3.12

import logging
from pathlib import Path

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S %s %Z %z',
  filemode='+at',
  filename=f'{Path(__file__).parent.parent.parent}/logs/python_data_classes_are_amazing_here_is_why.log'
)

logging.debug(f'Name of module is: {__name__}')
logging.debug(f'Path to module is: {__path__}')