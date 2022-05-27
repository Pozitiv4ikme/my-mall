from accounting import Accounting


class Electronics(Accounting.Customer.Good):
    function = "gaming headphones"
    name = "HyperX Cloud Stinger 2"
    producer = "HyperX"
    price_in_dollar = 110.49

    def __init__(self, function: str, name: str, producer: str, price_in_dollar: float) -> None:
        super().__init__(name, producer, price_in_dollar)
        self.function = function

    def __str__(self):
        return super(Electronics, self).__str__() \
               + f"function - {self.function}."
