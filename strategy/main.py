from .factories.PaymentStrategyFactory import PaymentStrategyFactory

def main():
    strategy = PaymentStrategyFactory().create('upi')
    strategy.pay()

main()