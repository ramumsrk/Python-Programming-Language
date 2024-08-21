#! /usr/bin/python3.12

import logging
from pathlib import Path

logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt='%Y-%m-%d %H:%M:%S %s %Z %z',
  filemode='+at',
  filename=f'{Path(__file__).parent.parent.parent}/logs/rethinking_the_need_for_abstract_classes_in_python.log'
)

logging.debug(f'Module name is: {__name__}')
logging.debug(F'Path to module is: {__path__}')