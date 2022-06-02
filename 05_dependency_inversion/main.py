"""Методы не должны зависеть от конкретных классов. Для этого мы выделили
авторизации в отдельный абстрактный класс и используем его в typing. А
затем реализуем необходимые классы авторизаций
"""

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


class Authorizer(ABC):

    @abstractmethod
    def is_authorized(self):
        pass


class SMSAuth(Authorizer):

    authorized = False

    def verify_code(self, code):
        print(f'Verifying SMS code: {code}')
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class NotARobot(Authorizer):

    authorized = False

    def not_a_robot(self):
        print('Not a robot')
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code


    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception('Not authorized')
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

    def __init__(self, email, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email = email

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception('Not authorized')
        print('Processing credit payment method')
        print(f'Verifying email: {self.email}')
        order.status = 'paid'


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())

authorizer = NotARobot()
processor = DebitPaymentProcessor('123456', authorizer)
authorizer.not_a_robot()
processor.pay(order)

authorizer = SMSAuth()
processor = PaypalPaymentProcessor('hi@gmail.com', authorizer)
authorizer.verify_code(567)
processor.pay(order)
