from typing import Any


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None]*size
    
    def __hash(self, key):
        my_hash = 0 
        for letter in key:
            my_hash = (my_hash + ord(letter)*23)%len(self.data_map)
        return my_hash
    
    def __str__(self,):
        string = ''
        for i, val in enumerate(self.data_map):
            string += f'{i} : {val}\n'
        return string
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item
        return None
    
    def keys(self):
        keys = []
        for item in self.data_map:
            if item:
                for key in item:
                    keys.append(key[0])
                    
        return keys



def has_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    combined_set = set1 | set2
    
    if len(combined_set) == len(set1) + len(set2):
        return False
    else:
        return True

def first_non_repeating_char(string):
    char_counts = {}
    for letter in string:
        char_counts[letter] = char_counts.get(letter, 0) + 1
    for letter in string:
        if char_counts[letter] == 1:
            return letter
    return None

my_hash_table = HashTable()
my_hash_table.set_item("bolts", 12)
my_hash_table.set_item("washers", 12)
print(my_hash_table)
print(my_hash_table.get_item("washers"))
print(my_hash_table.keys())

print(has_common([1, 1, 2,3 ], [1, 4, 5 ]))
print(has_common([1,1,  2,3 ], [4, 5 ]))

print(first_non_repeating_char("ls l"))

