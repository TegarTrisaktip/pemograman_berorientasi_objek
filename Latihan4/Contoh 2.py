class Menu:
    def __init__(self, dishes=None):
        if dishes is None:
            self.dishes = []
        else:
            self.dishes = dishes
    def add_dish(self, dish):
        self.dishes.append(dish)
        print("Menu",dish.name,dish.price)

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        print("Warung Padang")

dish1 = Dish("Nasi Telor", 12000)
dish2 = Dish("Nasi Rendang", 15000)
menu = Menu([dish1, dish2])
restaurant = Restaurant("Warung Padang", menu)
restaurant.menu.add_dish(dish1)
restaurant.menu.add_dish(dish2)
restaurant.menu.dishes 