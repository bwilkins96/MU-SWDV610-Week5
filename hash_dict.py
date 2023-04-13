# SWDV 610: Data Structures and Algorithms
# Simple hash table using a dictionary

class HashDict:
    """Simple hash table class that stores data in a dictionary"""
    def __init__(self, hash_val=1000):
        self._data = {}
        self._hash_val = hash_val

    def _hash(self, val):
        """Hashes a value using an accumulation of ordinal values"""
        acc = 0
        for char in str(val):
            acc += ord(char)

        return acc % self._hash_val
    
    def insert(self, val):
        """Inserts val into the data dictionary"""
        hash_idx = self._hash(val)
        self._data[hash_idx] = val
    
    def __repr__(self):
        return str(self._data)
    
    def __getitem__(self, i):
        return self._data[i]
    
if __name__ == '__main__':
    h_dict = HashDict()
    h_dict.insert(22)
    h_dict.insert(442)
    h_dict.insert(5)
    print(h_dict)

