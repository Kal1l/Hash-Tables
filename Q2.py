class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def linear_probing(self, key, i):
        return (self.hash_function(key) + i) % self.size

    def quadratic_probing(self, key, i):
        c1, c2 = 1, 3
        return (self.hash_function(key) + c1 * i + c2 * i**2) % self.size

    def double_hashing(self, key, i):
        h1 = self.hash_function(key)
        h2 = 1 + (key % (self.size - 1))
        return (h1 + i * h2) % self.size

    def insert(self, key, method="linear"):
        for i in range(self.size):
            if method == "linear":
                index = self.linear_probing(key, i)
            elif method == "quadratic":
                index = self.quadratic_probing(key, i)
            elif method == "double":
                index = self.double_hashing(key, i)
            if self.table[index] is None:
                self.table[index] = key
                return index
        raise Exception("Tabela hash cheia")

    def search(self, key, method="linear"):
        for i in range(self.size):
            if method == "linear":
                index = self.linear_probing(key, i)
            elif method == "quadratic":
                index = self.quadratic_probing(key, i)
            elif method == "double":
                index = self.double_hashing(key, i)
            if self.table[index] == key:
                return index
            if self.table[index] is None:
                return None
        return None

    def remove(self, key, method="linear"):
        index = self.search(key, method)
        if index is not None:
            self.table[index] = None
            return True
        return False

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}: {self.table[i]}")

# Demonstração
keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]
hash_table_linear = HashTableOpenAddressing(11)
hash_table_quadratic = HashTableOpenAddressing(11)
hash_table_double = HashTableOpenAddressing(11)

for key in keys:
    hash_table_linear.insert(key, method="linear")
    hash_table_quadratic.insert(key, method="quadratic")
    hash_table_double.insert(key, method="double")

print("Tentativa Linear:")
hash_table_linear.display()

print("\nTentativa Quadrática:")
hash_table_quadratic.display()

print("\nDispersão Dupla:")
hash_table_double.display()