"""
Project 3 - Binary Search Trees
I used AVL trees to work with trees
Uses two classes to store data
"""

class TreeSet:
    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """
    def __init__(self, comp):
        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """
        self.comp = comp
        self.length=0
        self.root=None
        # added stuff below
        self.success=False # variable to hold success 
                           # of remove or insert

    def __len__(self):
        # gets length
        return self.length 

    def height(self):
        # gets the height of a tree 
        if self.root is None:
            return - 1
        return self.root.hgt - 1

    def insert(self, item):
        # inserts an item to a tree
        # :param val:
        self.success = True
        # if it is already in the tree
        if item in self: #O(logn)
            self.success = False
        # not in the tree, so run recursive helper
        else: #O(logn)
            self.root = self.better_insert(self.root, item)
        # conditional len update
        if self.success is True:
            self.length+=1
        return self.success

    def remove(self, item):
        # removes a value from the tree
        # :param val:
        # success reset
        self.success = True
        # call the recursion and make root receive the new root
        self.root = self.recurse_remove(self.root, item)
        # if it removed an item, update len
        if self.success is True:
            self.length-=1
        return self.success

    def __contains__(self, item):
        # uses recursive helper to see if the tree contains a val
        return self.contains_help(self.root,item)

    def first(self):
        # uses helper function to find first val
        if self.length == 0:
            raise KeyError
        return self.first_help(self.root).data

    def last(self):
        # uses helper function to find last val
        if self.length == 0:
            raise KeyError
        return self.last_help(self.root).data

    def clear(self):
        # clears the BST 
        self.length = 0
        self.h = 0
        self.root = None

    def __iter__(self):
        # creates an iterator of the tree
        l = self.traverse(self.root)
        for i in l:
            yield i

    # Pre-defined methods

    def is_empty(self):
        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """
        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))

    # Helper functions
    # You can add additional functions here

    def contains_help(self, node, item):
        # recursion for getting if the tree contains a val
        if node is None:
            return False
        elif item == node:
            return True
        elif self.comp(item,node.data) > 0:
            return self.contains_help(node.right,item)
        return self.contains_help(node.left,item)

    def first_help(self, node):
        # recursion for getting first val
        if node.left is None:
            return node
        else:
            return self.first_help(node.left)

    def last_help(self, node):
        # recursion for getting the last val
        if node.right is None:
            return node
        else:
            return self.last_help(node.right)

    def traverse(self,node):
        # recursion method used with iter
        # does an in order traversal of the tree
        if node is not None:
            yield from self.traverse(node.left)
            yield node
            yield from self.traverse(node.right)

    def better_insert(self, node, item):
        # recursive helper function 
        # :param node(start with root) and value to insert:

        # normal insert
        if not node:
            return TreeNode(item)
        # compares with the given comparison function
        elif self.comp(item,node.data) < 0:
            node.left = self.better_insert(node.left, item)
        else:
            node.right = self.better_insert(node.right, item)
        # calc new height and balance of tree
        node.hgt = 1 + max(self.getNodeHeight(node.left),self.getNodeHeight(node.right))

        balance = self.getNodeBalance(node)

        # rebalance the tree
        # left left
        if balance > 1 and self.comp(item,node.left.data) < 0:
            return self.rightRotate(node)
        # right right 
        if balance < -1 and self.comp(item,node.right.data) > 0:
            return self.leftRotate(node)
        # left right
        if balance > 1 and self.comp(item,node.left.data) > 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        # right left
        if balance < -1 and self.comp(item,node.right.data) < 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def recurse_remove(self, node, item):
        """
        Helper function for removing a node from the tree
        :param node(starts with root) and item to remove:
        """
        # starts with removing the node
        if not node:# no node at this spot
            self.success = False
            return node
        elif self.comp(item,node.data) < 0:
            node.left = self.recurse_remove(node.left, item)
        elif self.comp(item,node.data) > 0:
            node.right = self.recurse_remove(node.right, item)
        else:# found the node to delete
            if node.left is None:
                tmp = node.right
                node = None
                return tmp

            elif node.right is None:
                tmp = node.left
                node = None
                return tmp

            tmp = self.left_leaf(node.right)
            node.data = tmp.data
            node.right = self.recurse_remove(node.right,
                                      tmp.data)
        # tree only had one node, return None
        if node is None:
            return node
        #calc height
        node.hgt = 1 + max(self.getNodeHeight(node.left),
                            self.getNodeHeight(node.right))
        # calc balance value
        balance = self.getNodeBalance(node)
        # left left tree rotation
        if balance > 1 and self.getNodeBalance(node.left) >= 0:
            return self.rightRotate(node)
        # right right rotation
        if balance < -1 and self.getNodeBalance(node.right) <= 0:
            return self.leftRotate(node)
        # left right
        if balance > 1 and self.getNodeBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        # right left
        if balance < -1 and self.getNodeBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

    def getNodeHeight(self, node):
        """
        get the height of a node
        necessary because if its none 
        the function will return 0 and not 
        cause an error
        :param TreeNode:
        """
        if node is None:
            return 0
        return node.hgt

    def getNodeBalance(self, node):
        #checks the balance
        if node is None:
            return 0
        return self.getNodeHeight(node.left) - self.getNodeHeight(node.right)

    def left_leaf(self, node):
        #finds a nodes min child
        if node is None or node.left is None:
            return node
        return self.left_leaf(node.left)

    def leftRotate(self, node):
        # performs a left tree rotation
        # save variables for usage
        new = node.right
        top = new.left
        # rotate it
        new.left = node
        node.right = top
    
        # update node heights
        node.hgt = 1 + max(self.getNodeHeight(node.left), 
                         self.getNodeHeight(node.right))
        new.hgt = 1 + max(self.getNodeHeight(new.left), 
                         self.getNodeHeight(new.right))
        # new root
        return new

    def rightRotate(self, node):
        # performs a right tree rotation
        # save variables for rotation
        new = node.left
        top = new.right

        # do the rotation
        new.right = node
        node.left = top

        # update the heights
        node.hgt = 1 + max(self.getNodeHeight(node.left),
                          self.getNodeHeight(node.right))
        new.hgt = 1 + max(self.getNodeHeight(new.left),
                          self.getNodeHeight(new.right))
        # return the new root
        return new


class TreeNode:
    """
    A node to be used by the TreeSet
    """
    def __init__(self, data):
        """
        Constructor
        You can add additional data as needed
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None
        self.hgt = 1 # each individual node saves its height
        # added stuff below

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'node({0})'.format(self.data)

    def __eq__(self, other): 
        # comparer to test if something is equal
        return self.data == other

