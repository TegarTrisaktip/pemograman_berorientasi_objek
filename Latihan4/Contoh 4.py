class RAM:
    def __init__(self, capacity):
        self.capacity = capacity
class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
        
ram = RAM(10)
storage = Storage(800)
computer = Computer(ram, storage)
print(computer.ram.capacity) 
print(computer.storage.capacity)