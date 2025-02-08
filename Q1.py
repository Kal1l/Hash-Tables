class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def remove(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}:", end=" ")
            current = self.table[i]
            if current is None:
                print("None")
            else:
                while current:
                    print(current.key, end=" -> " if current.next else "")
                    current = current.next
                print()

# Demonstração
keys = [5, 28, 19, 15, 20, 33, 12, 17, 10]
hash_table = HashTable(9)

for key in keys:
    hash_table.insert(key)

print("Tabela Hash com Encadeamento Exterior:")
hash_table.display()