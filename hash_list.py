# SWDV 610: Data Structures and Algorithms
# Simple hash table using a list

class HashList:
    """Simple hash table class that stores data in a list"""
    def __init__(self, size=11):
        self._data = [None] * size

    def _hash(self, val):
        """Hashes a value using the mid-square method"""
        square_str = str(val**2)
        start = len(square_str) // 3
        stop = len(square_str) // 2 + 1
        mid_square = int(square_str[start:stop])

        return mid_square % len(self._data)
    
    def insert(self, val):
        """Inserts val into the data list"""
        hash_idx = self._hash(val)
        self._data[hash_idx] = val
    
    def __repr__(self):
        return str(self._data)
    
    def __getitem__(self, i):
        return self._data[i]
    
if __name__ == '__main__':
    h_list = HashList()
    h_list.insert(22)
    h_list.insert(442)
    h_list.insert(5)
    print(h_list)


