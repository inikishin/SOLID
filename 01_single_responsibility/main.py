"""В данном случае мы разделили логику между классами Заказ и Процесс оплаты.
Если мы захотим добавить новый метод оплаты, напр. ПейПал, то нам не
потребуется изменять класс Заказа.
"""

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


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print('Processing debit payment method')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'

    def pay_credit(self, order, security_code):
        print('Processing credit payment method')
        print(f'Verifying security code: {security_code}')
        order.status = 'paid'



order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())

processor = PaymentProcessor()
processor.pay_credit(order, '123456')
