from abc import ABC, abstractmethod

class Receiver:
    def __init__(self, bank_transfer: bool = False, money_transfer: bool = False, paypal_transfer: bool = False) -> None:
        self.bank_transfer = bank_transfer
        self.money_transfer = money_transfer
        self.paypal_transfer = paypal_transfer


class PaymentHandler(ABC):
    def __init__(self) -> None:
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    @abstractmethod
    def handle(self, receiver):
        if self.successor:
            self.successor.handle(receiver)

class BankPaymentHandler(PaymentHandler):
    def handle(self, receiver):
        if receiver.bank_transfer:
            print("Выполняем банковский перевод")
        else:
            super().handle(receiver)

class MoneyPaymentHandler(PaymentHandler):
    def handle(self, receiver):
        if receiver.money_transfer:
            print("Выполняем перевод через системы денежных переводов")
        else:
            super().handle(receiver)

class PayPalPaymentHandler(PaymentHandler):
    def handle(self, receiver):
        if receiver.paypal_transfer:
            print("Выполняем перевод через PayPal")
        else:
            super().handle(receiver)


if __name__ == "__main__":
    receiver = Receiver(bank_transfer=False, money_transfer=True, paypal_transfer=True)

    # Создаем обработчики
    bank_handler = BankPaymentHandler()
    money_handler = MoneyPaymentHandler()
    paypal_handler = PayPalPaymentHandler()

    # Устанавливаем цепочку обязанностей
    bank_handler.set_successor(paypal_handler)
    paypal_handler.set_successor(money_handler)

    # Запускаем обработку
    print("Обработка платежа:")
    bank_handler.handle(receiver)
