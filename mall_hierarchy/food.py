from good import Good


class Food(Good):

    def __init__(self, expiration_date: str = "26.05.2023", name: str = "potato pancakes", producer: str = "Our sign",
                 price_in_dollar: float = 3.15) -> None:
        super().__init__(name, producer, price_in_dollar)
        self.expiration_date = expiration_date

    def __str__(self):
        return super(Food, self).__str__() \
            + f"expiration date - {self.expiration_date}."
