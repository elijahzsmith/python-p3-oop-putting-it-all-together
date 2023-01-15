#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size=0):
        self.brand = brand
        self.size = size

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def get_size(self):
        return self._size

    def set_size(self, size):
        if type(size) is int:
            self._size = size

    size = property(get_size, set_size)