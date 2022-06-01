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
