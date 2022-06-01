class Accounting:
    time_to_do = "15.03.2004"

    def __init__(self, time_to_do: str) -> None:
        self.time_to_do = time_to_do

    def accounting(self, customer, good):
        price_for_all = customer.amount_of_good * good.price_in_dollar
        print(f"{customer.name_of_customer}, you spent {price_for_all}$ for {good.name}! Information about "
              f"{self.time_to_do}.")
