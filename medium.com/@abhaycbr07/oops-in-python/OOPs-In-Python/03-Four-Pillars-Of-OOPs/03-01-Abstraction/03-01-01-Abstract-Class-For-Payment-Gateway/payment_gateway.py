#! /usr/bin/python3.12

from abc import ABC , abstractmethod

class PaymentGateway(ABC):
  @abstractmethod
  def process_payment( self , * , amount : float ):
    pass
  @abstractmethod
  def refund_payment( self , * , transaction_id : int , amount : float ):
    pass
  @abstractmethod
  def get_payment_status( self , * , transaction_id : int ):
    pass