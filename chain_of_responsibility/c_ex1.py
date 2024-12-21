from ex_1 import Receiver, PayPalPaymentHandler, BankPaymentHandler, MoneyPaymentHandler

if __name__ == "__main__":
    # Новая последовательность: сначала PayPal, потом банк, затем денежные переводы
    receiver = Receiver(bank_transfer=True, money_transfer=False, paypal_transfer=False)

    paypal_handler = PayPalPaymentHandler()
    bank_handler = BankPaymentHandler()
    money_handler = MoneyPaymentHandler()

    paypal_handler.set_successor(bank_handler)
    bank_handler.set_successor(money_handler)

    print("Обработка платежа с новой последовательностью:")
    paypal_handler.handle(receiver)

    # Тестируем другую комбинацию параметров Receiver
    receiver = Receiver(bank_transfer=False, money_transfer=True, paypal_transfer=False)
    print("\nОбработка платежа с новой комбинацией параметров:")
    paypal_handler.handle(receiver)
