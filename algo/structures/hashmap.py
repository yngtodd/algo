from collections import namedtuple
from algo.structures import LinkedList


KeyValue = namedtuple('KeyValue', ['key', 'value'])


class HashMap:

    def __init__(self, len_array: int):
        self.len_array = len_array
        self.map = self.create_map(len_array)

    def create_map(self, len_array: int):
        r"""Create array for hashmap

        Args:
            len_array: length of the array to use for the
                       hashmap.
        """
        return [LinkedList() for _ in range(len_array)]

    def hash_function(self, key: str):
        r"""Hash for the location to place data in the array

        Args:
            key: the key to be stored in the hashmap
        """
        ascii_values = [ord(char) for char in key]
        return sum(ascii_values) % self.len_array

    def add(self, key, value):
        r"""Add a key-value pair in hashmap"""
        hash_value = self.hash_function(key)
        key_value = KeyValue(key, value)
        self.map[hash_value].append(key_value)

    def get(self, key):
        r"""Retrieve a value

        Args:
            key: key that was used to hash the data
        """
        hash_value = self.hash_function(key)
        linked_list = self.map[hash_value]

        for key_value in linked_list:
            if key_value.key == key:
                return key_value.value

        return None

    def delete(self, key):
        r"""Delete a value

        Args:
            key: key to the retrieve the value
        """
        hash_value = self.hash_function(key)
        linked_list = self.map[hash_value]

        for key_value in linked_list:
            if key_value.key == key:
                linked_list.delete(key_value)


