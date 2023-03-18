

from abc import ABC, abstractmethod
class checkout(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: $", amount)
# I kept paySlip because from what was described in step 280, abstract methods are most commonly used for payment
    @abstractmethod # It looks like this is a decorator that abstracts def payment() in paySlip
    def payment(self, amount):
        pass

class GiftCardPayment(checkout):
#   Here, we've defined how to implement the payment function from its parent paySlip class
    def payment(self, amount):
        print('Your Gift Card payment was accepted for $250. Your remaining balance is ${}.'.format(amount - 250))

obj = GiftCardPayment()
obj.paySlip(400)
obj.payment(400)
