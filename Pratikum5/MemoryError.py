try:
    data = "23" * (10**10)
except MemoryError:
    print("Memori tidak cukup untuk menampung data yang diminta!")