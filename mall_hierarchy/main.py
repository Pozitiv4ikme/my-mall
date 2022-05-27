from accounting import Accounting
from electronics import Electronics
from food import Food
from furniture import Furniture
from mall import Mall
from store import Store

if __name__ == '__main__':
    my_first_mall = Mall("Paradise", 9, 30, 23, 30)
    my_first_store = Store("Puma", "sportswear", 10, 00, 22, 30)
    sportswear = Accounting.Customer.Good("sport pants", "Puma", 12.5)
    fitness_tracker = Electronics("fitness tracker", "XIAOMI Mi Band 6 SmartBand", "Xiaomi", 99.99)
    protein = Food("one year after opening the package", "Whey 100", "Whey", 25.20)
    horizontal_bar_for_pulling_up = Furniture("sport", "Just do it!", "Nike", 150)
    accounting = Accounting("Vitalii", 100, "food", "chocolate bar", "MilkyWay", 2.75)

    print(my_first_mall)
    print(my_first_store)
    print(sportswear)
    print(fitness_tracker)
    print(protein)
    print(horizontal_bar_for_pulling_up)

    accounting.accounting()
