from .PaymentStrategy import PaymentStrategy

class UpiPayment(PaymentStrategy):
    def pay(self):
        print("Upi payment")