class HashTable:
    def __init__(self, size=7013):
        """
        Created an instance of a hash table

        :parm        size: The size you want the hash table to initially be, should be a prime. Set to 7013 if left blank
        :pre         size must be an integer and should be a prime for best perfromace
        :post        an empty instance of a hash table is created 
        :complexity  best = worst: O(1)  
        """
        self._count = 0
        self._array = [None] * size
        self._table_size = size 

    def __setitem__(self, key, item):
        """
        Sets an item in the table

        :param      key: a string value to identify the item being put in the table
        :param      item: the item you want to put into the table with the associated key 
        :retrun     N/A
        :pre        the key must be a string type
        :post       the item is placed in the position given by the hash value of the key, if its full, then the next
                    available spot 
        :complexity best: O(1)*
                    worst: O(n) where n is the size of the hash table       
        """
        # getting item position by hashing key
        pos = self.hash(key)

        for _ in range(self._table_size):
            # if position is empty
            if self._array[pos] is None:
                self._array[pos] = (key, item)
                self._count += 1
                return 
            # if key is in use, update with new item
            elif self._array[pos][0] == key:
                self._array[pos] = (key, item)
                return 
            else:
                # if full go to next position
                pos = (pos + 1) % self._table_size
        # resizing if full
        self.rehash()
        self[key] = item

    def __getitem__(self, key):
        """
        Returns an item in the table at a given key

        :parm       key: a string to identifying the item you are searching for
        :return     the item correspoding with the given key
        :pre        the key must already be in the table 
        :pre        key must be a string type
        :post       the table is not changed in any way
        :complexity best: O(1)
                    worst: O(n) where n is the size of the table
        """
        # getting item position by hashing key
        pos = self.hash(key)

        for _ in range(self._table_size):
            # if key does not exist in table
            if self._array[pos] is None:
                raise KeyError(key)
            # if key is in table
            elif self._array[pos][0] == key:
                return self._array[pos][1]
            # not the correct key so keep searching 
            else:
                pos = (pos + 1) % self._table_size
        
        raise Exception('key not found')

    def __contains__(self, key):
        """
        Returns if a key is in the table

        :param      key: the key you are looking for in the table
        :return     True if the key is in the table, else False
        :pre        key must be a string 
        :complexity best: O(1)
                    worst: O(n) where is is the size of the table
        """
        pos = self.hash(key)

        for _ in range(self._table_size):
            if self._array[pos] is None:
                return False
            elif self._array[pos][0] == key:
                return True
            else:
                pos = (pos + 1) % self._table_size
        
        return False
        
    def hash(self, key):
        """
        Creates a hash for a given key

        :param       key: a string value which you want to calculate a hash value for
        :return      the hash value for that key
        :pre         key must be a string
        :post        the returned hash value is a string
        :complexity  best = worst: O(n) where n is the number of characters in key       
        """
        if type(key) is not str:
            raise ValueError('key must be a sting')

        value = 0
        a = 31415
        b = 27183
        for char in key:
            value = (ord(char) + a*value) % self._table_size
            a = a * b % self._table_size

        return value

    def rehash(self):
        """
        Increases the size of the hash table table

        :pre        a hash table must be defined 
        :pre        the table must be full
        :post       new size will be the lowest prime that is at least double the previous size
        :post       all keys are put into the table but are rehashed so in a new position 
        :complexity best = worst: O(n) where is is the size of the table
        """
        primes = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761,
            919, 1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591,
            17519, 21023, 25229, 30293, 36353, 43627, 52361, 62851, 75431, 90523, 108631, 130363, 156437,
            187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263,
            1674319, 2009191, 2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369
        ]

        # finding new size from list of primes
        i = 0
        while primes[i] < self._table_size * 2:
            # raise exception if no larger prime found
            if i + 1 >= len(primes):
                raise ValueError('No prime large enough for resize') 
            new_table_size = primes[i + 1]
            i += 1

        # resetting table to new size
        old_table_size = self._table_size
        old_array = self._array
        self._table_size = new_table_size
        self._array = [None] * self._table_size
        self._count = 0

        # rehashing everything in current array and putting it in new one
        for i in range(old_table_size):
            if old_array[i] is not None:
                self[old_array[i][0]] = old_array[i][1]

