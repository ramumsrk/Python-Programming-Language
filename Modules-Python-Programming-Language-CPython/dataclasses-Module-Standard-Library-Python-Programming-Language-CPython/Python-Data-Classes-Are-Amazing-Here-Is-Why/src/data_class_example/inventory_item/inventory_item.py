#! /usr/bin/python3.12

from typing import Self, Literal
from dataclasses import dataclass

@dataclass
class InventoryItem:
  '''
  A class representing an Item in an Inventory
  '''
  # Instance fields
  item_name: str
  item_unit_price: float
  items_quantity_on_hand: int = Literal[0]
  # Instance method
  def total_cost(self: Self) -> float:
    '''
    Return the total cost of all items in an inventory
    '''
    return self.item_unit_price * self.items_quantity_on_hand