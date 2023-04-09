# Nama : Tegar Trisakti Pamungkas
# Kelas : R1
# Nim : 210511029

class Perusahaan:
    def __init__(self,name):
        self.name = name
        self.karyawan = Karyawan()
        print("PT. Freeport")

class Data:
    def __init__(self, name, sience, placed):
        self.name = name
        self. sience = sience
        self. placed = placed

class Karyawan:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Nama:", item.name, "Sejak", item.sience, "Bagian",item.placed)

    def remove_item(self, item):
        self.items.remove(item)


Perusahaan = Perusahaan("PT. Freeport")
data1 = Data("Tegar Trisakti pamungkas",2021, "IT")
data2 = Data("Rifki Fadilah", 2022, "sipil")
Perusahaan.karyawan.add_item(data1)
Perusahaan.karyawan.add_item(data2)
Perusahaan.karyawan.items