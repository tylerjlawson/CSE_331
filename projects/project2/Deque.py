"""
Project 2 - Deques
Tyler Lawson
Classes set up as a linked list to be a functional deque 
"""

class Node(object):
    """
    A Node class so that each node in the Deque can easily 
    store its own information: data, next node, and prev node
    """
    def __init__(self, data=None, next_node=None, prev_node=None):
        """
        initializes a node that defaults to empty
        param: data, next_node, or prev_node can be set at initialization
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class Deque:
    """
    A double-ended queue
    that uses a linked list
    """

    def __init__(self):
        """
        Initializes an empty Deque
        has size var to make len operate as O(1)
        has head and tail to know the ends of the deque
        """
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        """
        Computes the number of elements in the Deque
        :return: The logical size of the Deque
        O(1)
        """
        return self.size # returns the variable that has tracked the size

    def peek_front(self):
        """
        Looks at, but does not remove, the first element
        :return: The first element
        O(1)
        """
        if (self.is_empty()): #check if it is empty
            raise IndexError # index error for empty deque
        return self.head.data

    def peek_back(self):
        """
        Looks at, but does not remove, the last element
        :return: The last element
        O(1)
        """
        if (self.is_empty()): #check if it is empty
            raise IndexError # index error for empty deque
        return self.tail.data

    def push_front(self, e):
        """
        Inserts an element at the front of the Deque
        :param e: An element to insert
        O(1)
        """
        if (self.is_empty()): # if empty set head and tail to new node
            self.head = Node(e)
            self.tail = self.head
        else: # case of not empty deque
            new_node = Node(e, self.head) # initialize node to add with its next as the old head
            self.head.prev_node = new_node # set old head prev node to new head 
            self.head = new_node # set the new head to head
        self.size += 1 # update the size 

    def push_back(self, e):
        """
        Inserts an element at the back of the Deque
        :param e: An element to insert
        O(1)
        """
        if (self.is_empty()): # when there is an empty deque
            self.head = Node(e)
            self.tail = self.head
        else: # when the deque has contents
            new_node = Node(e, None, self.tail) # make new node with the old tail as its prev node
            self.tail.next_node = new_node # update the old tail to point to new tail
            self.tail = new_node # set new tail as the deque tail
        self.size += 1 # update the size
        
    def pop_front(self):
        """
        Removes and returns the first element
        :return: The (former) first element
        O(1)
        """
        if (self.is_empty()):# check for empty deque
            raise IndexError
        elif(self.size==1): # special case of deque with 1 node
            old_head = self.head # return node
            self.clear() # clear removest the one node
        else: # case of more than 
            old_head = self.head # return node
            self.head = self.head.next_node # update pointers
            self.tail.next_node = None
            self.size -= 1 #update size
        return old_head.data # returns the value removed from the deque
        
    def pop_back(self):
        """
        Removes and returns the last element
        :return: The (former) last element
        O(1)
        """
        if (self.is_empty()): # error check
            raise IndexError
        elif(self.size==1): # special case
            old_tail = self.tail # return node
            self.clear()
        else: # more than one node deque
            old_tail = self.tail # return node
            self.tail = self.tail.prev_node #update poitners
            self.tail.next_node = None
            self.size -= 1 #update size
        return old_tail.data #return val removed
       
    def clear(self):
        """
        Removes all elements from the Deque
        :return:
        O(n)
        """
        while(self.size > 1): # pops all items except the last
            self.pop_front()

        #this takes care of the last node
        self.head = None 
        self.tail = None
        self.size = 0

    def retain_if(self, condition):
        """
        Removes items from the Deque so that only items satisfying the given condition remain
        :param condition: A boolean function that tests elements
        O(n)
        """
        iter_node = self.head # temp node to use to iterate through deque
        while (iter_node != None): # when it is none, done looking through deque
            if not (condition(iter_node.data)): # when false, remove from deque
                if (iter_node == self.head): # when it is the head pop front
                    self.pop_front()
                elif(iter_node == self.tail): # when it is the tail pop back
                    self.pop_back()
                else: # when it is somewhere in the middle set pointers from right and left to skip node
                    iter_node.prev_node.next_node = iter_node.next_node
                    iter_node.next_node.prev_node = iter_node.prev_node
                    self.size -= 1 # update size
            iter_node = iter_node.next_node # iterate to the next node

    def __iter__(self):
        """
        Iterates over this Deque from front to back
        :return: An iterator
        O(n)
        """
        iter_node = self.head # use to iterate through deque
        while (iter_node != None):
            yield iter_node.data # yield to the iterator, the data
            iter_node = iter_node.next_node #iterate to the next

    # provided functions

    def is_empty(self):
        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this Deque
        :return: A string
        """
        return 'Deque([{0}])'.format(','.join(str(item) for item in self))

