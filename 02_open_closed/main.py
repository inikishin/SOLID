"""Если мы захотим добавить новый метод оплаты, но нам пришлось бы модифицировать
класс PaymentProcessor. Чтобы этого избежать создается структура подклассов,
которые реализуют необходимые методы.

Т.е. класс становится открытым для расширения, но закрытым для изменения. Если
мы захотим добавить еще методов оплаты, то нам не потребуется вносить изменения
в основной класс PaymentProcessor.
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


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing debit payment method')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing credit payment method')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print('Processing credit payment method')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())

processor = DebitPaymentProcessor()
processor.pay(order, '123456')
