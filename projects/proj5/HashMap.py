# Project 5 - Hashmap
# Use a hash table to store keys with values
# Uses List class to implement hash table
# Uses linear probing to solve collisions

class HashMap:
    """
    Class is built as a hash table that uses lists
    """
    def __init__(self, load_factor=1.00):
        self.max_load_factor = load_factor
        self.size = 20
        self.tups = [None] * self.size
        self.keylist = []

    def __len__(self): # Returns number of key value pairs in the hashmap
        return len(self.keylist)

    def load(self): # load factor = num of elements / size of hashmap
        return (len(self)/self.size)

    def __contains__(self, key): # returns true if key in hashmap
        return key in self.keylist

    def __getitem__(self, key):
        # Returns value given a specific key
        if self.is_empty():  # Error check 
            raise KeyError(key)
        start = self.hash(key) # start at the hash value
        pos = start # save the start position
        while self.tups[pos] is not None: # iterate through to find element
            if self.tups[pos][0] == key: # found key
                return self.tups[pos][1]
            else: # go to next key cause of linear probing
                pos += 1
                if pos == start:
                    raise KeyError(key)
                elif pos == self.size:
                    pos = 0

        raise KeyError(key)

    def __setitem__(self, key, value):
        """
        Takes a key and value pair to set a new element 
        or update the value of an existing key
        """
        hash_val = self.hash(key) 
        # check if normal location is open
        if self.tups[hash_val] is None or self.tups[hash_val] == 'removed':
            self.keylist.append(key)
            self.tups[hash_val] = (key,value)
        else:
            if self.tups[hash_val][0] == key: # this would update existing
                self.tups[hash_val] = (self.tups[hash_val][0], value)
            else: # linear probe to find next open spot
                new = hash_val + 1
                if new == self.size: # go to start when at end
                    new = 0
                while self.tups[new] is not None and self.tups[new] != 'removed'\
                             and self.tups[new][0] != key: 
                             # search for spot to change
                    new += 1
                    if new == self.size:
                        new = 0
                if self.tups[new] is None or self.tups[new] == 'removed':
                    # can reassign full new spot
                    self.keylist.append(key)
                    self.tups[new] = (key,value)

                else: # updates existing value
                    self.tups[new] = (self.tups[new][0], value)

        if len(self) >= (self.size * self.max_load_factor):
            # increases size of the table if necessary
            self.resize(True)

    def __delitem__(self, key):
        """
        Does a lazy delete of items 
        Finds the item, places 'removed' in place of old tuple
        removes key from keylist
        """
        if self.is_empty(): # error check
            raise KeyError(key)
        start = self.hash(key) # start at hash function position
        pos = start
        while self.tups[pos] is not None:
            if self.tups[pos][0] == key: # set to 'removed'
                self.tups[pos] = 'removed'
                self.keylist.remove(key) # take out of bank of keys
                break
            else: # go to next spot if necessary due to linear probing
                pos += 1
                if pos == start:
                    break
                if pos == self.size: # check if at end of table
                    pos = 0

        if len(self) <= ((self.size * self.max_load_factor)/10) and len(self) > 0:
            # shrinks table if necessary
            self.resize(False)

    def __iter__(self): # returns iterator of all used pairs in the table
        for tup in self.tups:
            if tup is not None and tup is not 'removed':
                yield tup

    def clear(self): # clears out all of the existing elements in the hashmap
        self.size = 20
        self.tups = [None] * self.size
        self.keylist = []

    def keys(self): # returns a set of all the keys in use
        return set(self.keylist)

    # supplied methods

    def __repr__(self):
        return '{{{0}}}'.format(','.join('{0}:{1}'.format(k, v) for k, v in self))

    def __bool__(self):
        return not self.is_empty()

    def is_empty(self):
        return len(self) == 0

    # Helper functions can go here

    def hash(self, key): # hash function for indexing
        return hash(key)%self.size

    def resize(self, inc): 
    # resizes the hashmap to satisfy load factor requirements
    # param inc is a Boolean that decides to grow or shring the map
        save_tups = self.tups
        if inc: # grow the hashmap
            self.size *= 2
        else: # shrink
            self.size /= 2
        self.size = int(self.size)
        self.tups = [None] * self.size
        self.keylist = []
        for tup in save_tups:
            if tup is not None and tup != 'removed': 
                self[tup[0]] = tup[1]

def word_frequency(seq):
    """
    takes in an iterable and creates a hashmap with each of the
    words in the iterable with their values being the count
    of that word in the iterable
    then returns the result hashmap
    """
    hashmap = HashMap()
    for word in seq:
        if word not in hashmap:
            hashmap[word] = 1
        else:
            hashmap[word] = hashmap[word] + 1
    return hashmap