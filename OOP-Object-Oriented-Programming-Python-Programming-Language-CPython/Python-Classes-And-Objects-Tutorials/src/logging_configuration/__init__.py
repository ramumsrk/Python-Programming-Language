#! /usr/bin/python3.12

import logging
from pathlib import Path

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S.%s %Z %z',
  filemode='+at',
  filename=f'{Path(__file__).parent.parent.parent}/logs/python_classes_and_objects_tutorials.log'
)

logging.debug(f'Name of module is: {__name__}')
logging.debug(f'Path to module is: {__path__}')