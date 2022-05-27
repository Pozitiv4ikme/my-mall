class Accounting:
    class Customer:
        class Good:
            name = "chips"
            producer = "Lays"
            price_in_dollar = 1.98

            def __init__(self, name_of_good: str, producer_of_good: str, price_in_dollar: float) -> None:
                self.name = name_of_good
                self.producer = producer_of_good
                self.price_in_dollar = price_in_dollar

            def __str__(self):
                return f"The name of a product - {self.name}; producer - {self.producer}; price in dollar - " \
                       f"{self.price_in_dollar}; "

        name_of_customer = "Oleh"
        amount_of_good = 16
        type_of_product = "food"

        def __init__(self, name_of_customer: str, amount_of_good: int, type_of_good: str) -> None:
            self.name_of_customer = name_of_customer
            self.amount_of_good = amount_of_good
            self.type_of_product = type_of_good

        def __str__(self):
            return f"Name of customer - {self.name_of_customer}; amount of product - {self.amount_of_good}; type of " \
                   f"product - {self.type_of_product}."

    def __init__(self, name_of_customer, amount_of_good, type_of_good, name_of_good, producer_of_good,
                 price_in_dollar) -> None:
        self.some_customer = Accounting.Customer(name_of_customer, amount_of_good, type_of_good)
        self.some_good = Accounting.Customer.Good(name_of_good, producer_of_good, price_in_dollar)

    def accounting(self):
        price_for_all = self.some_customer.amount_of_good * self.some_good.price_in_dollar
        print(f"{self.some_customer.name_of_customer}, you spent {price_for_all}$ for {self.some_good.name}!")
