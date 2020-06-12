"""
Simple Hash Table

Assumptions:
    - keys are integers only
    - For collision resolution use chaining
    - Fixed length of the underlying array
"""


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{} -> {}".format(self.key, self.value)


class SimpleHashTable:

    def __init__(self, length):
        self.length = length
        self.table = [[] for _ in range(self.length)]

    def _hash_function(self, key):
        return key % self.length

    def set(self, key, value):
        new_item = Item(key, value)
        computed_hash = self._hash_function(key)
        for item in self.table[computed_hash]:
            if item.key == key:  # when using the same key twice, data is overwritten
                item.value = value

        self.table[computed_hash].append(new_item)

    def get(self, key):
        computed_hash = self._hash_function(key)
        for item in self.table[computed_hash]:
            if item.key == key:
                return item


if __name__ == "__main__":
    hash_table = SimpleHashTable(10)
    hash_table.set(12, "Hello world")
    hash_table.set(13, "Once upon the time, there lived a Python!")
    hash_table.set(22, "Once upon the time, there lived a Python!")
    print(hash_table.get(12))
    print(hash_table.get(22))
    hash_table.set(12, "I can add the same key one more time")
    print(hash_table.get(12))
