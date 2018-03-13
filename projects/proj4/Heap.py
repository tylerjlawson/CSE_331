"""
Project 4 - Heaps
Make an operational priority queue heap
use the heaps to find the median of a sequence
"""

class Heap:
    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self, comp):
        """
        Constructor
        :param comp: A comparison function determining the priority of the included elements
        """
        self.comp = comp
        # Added Members
        self.size = 0
        self.arr = []

    def __len__(self): # finds the size of a heap
        return len(self.arr)

    def peek(self): # finds the highest priority item in heap
        if self.is_empty(): # error check 
            raise IndexError
        return self.arr[0]

    def insert(self, item):
        """
        Inserts an element into a heap
        param is an element to insert
        """
        i = len(self) # counter
        self.arr.append(None) # add new blank spot for inserted element
        while i > 0 and self.comp(item,self.arr[self.parent(i)]):
            # reposition everything correctly
            self.arr[i] = self.arr[self.parent(i)]
            i = self.parent(i) # go to next element up in the heap
        self.arr[i] = item # reassign with new element

    def extract(self):
        """
        Removes the highest priority item from a heap 
        reorganizes everything with heapify after
        """
        if self.is_empty(): # error check 
            raise IndexError
        result = self.arr[0] # save the element removed for return
        self.arr[0] = self.arr[-1] # Move last to root H.size -= 1
        self.arr.pop() # remove extra space in heap
        self.heapify(0) # reorganize
        return result

    def extend(self, seq): # adds all items to a heap from a sequence
        for i in seq:
            self.insert(i)
        
    def clear(self): # clears the heap
        self.arr = []

    def __iter__(self):
        for i in range(len(self)):
            yield self.arr[i]

    # Supplied methods

    def __bool__(self):
        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """
        return not self.is_empty()

    def is_empty(self):
        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this heap
        :return:
        """
        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    # Added methods

    def heapify(self, i):
        """
        reorganizes a heap to be a valid heap
        param an index at which to start reorganizing
        """
        l = self.left(i) # save children
        r = self.right(i)
        if l < len(self.arr) and self.comp(self.arr[l], self.arr[i]):
            small = l 
        else:
           small = i
        if r < len(self.arr) and self.comp(self.arr[r], self.arr[small]):
            small = r 
        if small != i:
           self.arr[i], self.arr[small] = self.arr[small], self.arr[i] #Swap
           self.heapify(small)

    def parent(self, i): # finds parent index
        return int((i-1)/2)

    def left(self, i): # gets left child index
        return int((2*i)+1)

    def right(self, i): # gets right child index
        return int((2*i)+2)

# Required Non-heap member function

def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.
    :param seq: an iterable sequence
    :return: the median element
    """
    if not seq: # error check
        raise IndexError
    min_heap = Heap(lambda a, b: a <= b)
    max_heap = Heap(lambda a, b: a >= b)
    med = seq[0] # start value for calculated median
    for i in range(len(seq)): # go through list and calculate median
        med = median_help(seq[i], med, max_heap, min_heap)
    return med

def median_help(ele, the_median, maxH, minH):
    """
    takes a new element to add to the heaps
    adds to either the max or min heap to eventually have the 
    median be what is on top of the heaps after it has gone through the 
    whole list
    the balance will make it possible for the median to be on top
    """
    if len(maxH) == len(minH): # case of balanced heaps
        if ele < the_median: 
            maxH.insert(ele)
            the_median = maxH.peek()
        else: 
            minH.insert(ele)
            the_median = minH.peek()
    elif len(maxH) > len(minH): # case of max heap size larger
        if ele < the_median:
            minH.insert(maxH.extract())
            maxH.insert(ele)
        else:
            minH.insert(ele)
        the_median = minH.peek()
    else: # case of min heap of larger size
        if ele < the_median:
            maxH.insert(ele)
        else:
            maxH.insert(minH.extract())
            minH.insert(ele)
        the_median = minH.peek()
    return the_median


