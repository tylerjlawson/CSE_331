

class HashMap:
    def __init__(self, load_factor=1.00):
        # You may change the default maximum load factor
        self.max_load_factor = load_factor
        # Other initialization code can go here

    def __len__(self):
        return 0

    def load(self):
        return 0.0

    def __contains__(self, key):
        return False

    def __getitem__(self, key):
    	# Returns value types
        raise KeyError(key)

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        raise KeyError(key)

    def __iter__(self):
        while False:
        	yield None # Yield key-value pairs

    def clear(self):
        pass

    def keys(self):
        return set()

    # supplied methods

    def __repr__(self):
        return '{{{0}}}'.format(','.join('{0}:{1}'.format(k, v) for k, v in self))

    def __bool__(self):
        return not self.is_empty()

    def is_empty(self):
        return len(self) == 0

    # Helper functions can go here


# Required Function
def word_frequency(seq):
    return HashMap()
