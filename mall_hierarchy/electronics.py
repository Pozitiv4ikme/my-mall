from good import Good


class Electronics(Good):

    def __init__(self, function: str = "gaming headphones", name: str = "HyperX Cloud Stinger 2",
                 producer: str = "HyperX", price_in_dollar: float = 110.49) -> None:
        super().__init__(name, producer, price_in_dollar)
        self.function = function

    def __str__(self):
        return super(Electronics, self).__str__() \
               + f"function - {self.function}."
