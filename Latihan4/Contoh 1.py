# Nama : Tegar Trisakti Pamungkas
# Kelas : R1
# Nim : 210511029

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        print("Pretty Nana")
        
class Item:
    def __init__(self, name):
        self.name = name

class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        print("item",item.name)
    def remove_item(self, item):
        self.items.remove(item)

player = Player("Pretty Nana")
sword = Item("Immortal")
shield = Item("Shield")

player.inventory.add_item(sword)
player.inventory.add_item(shield)
player.inventory.items 