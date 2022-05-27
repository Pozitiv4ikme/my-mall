from accounting import Accounting


class Food(Accounting.Customer.Good):
    expiration_date = "26.05.2023"
    name = "potato pancakes"
    producer = "Our sign"
    price_in_dollar = 3.15

    def __init__(self, expiration_date: str, name: str, producer: str, price_in_dollar: float) -> None:
        super().__init__(name, producer, price_in_dollar)
        self.expiration_date = expiration_date

    def __str__(self):
        return super(Food, self).__str__() \
            + f"expiration date - {self.expiration_date}."
