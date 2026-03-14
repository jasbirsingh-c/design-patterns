from ..strategies.UpiPayment import UpiPayment

class PaymentStrategyFactory:
    def create(self, type):
        return UpiPayment()