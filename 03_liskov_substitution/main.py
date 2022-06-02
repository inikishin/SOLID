from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]

        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code


    def pay(self, order):
        print('Processing debit payment method')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print('Processing credit payment method')
        print(f'Verifying security code: {self.security_code}')
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email):
        self.email = email

    def pay(self, order):
        print('Processing credit payment method')
        print(f'Verifying email: {self.email}')
        order.status = 'paid'


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())

processor = DebitPaymentProcessor('123456')
processor.pay(order)

processor = PaypalPaymentProcessor('hi@gmail.com')
processor.pay(order)
