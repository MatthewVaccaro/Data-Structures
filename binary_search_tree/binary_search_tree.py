"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Self is equal to the root = Everything is compared to self
        # Steps
        # Create the new node being inserted
        newNode = BSTNode(value)
        # Compare the node to the root
        # if Greater compare to roots right value
        if newNode.value >= self.value:
            # If root Right value is None - Place Node
            if self.right == None:
                self.right = newNode
            # Else root.right.insert(NewNode) - Run recursion
            else:
                self.right.insert(value)
        # else Lesser compare to the roots left value
        else:
            if self.left == None:
                self.left = newNode
            # If root Left value is None - Place Node
            else:
                self.left.insert(value)
            # Else root.left.insert(NewNode) - Run recursion

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Steps
        # Compare value to Root
        if target == self.value:
            return True
        # If Greater check Right
        if target > self.value:
            # if right is none return False
            if self.right == None:
                return False
            # elif right == target return true
            elif self.right.value == target:
                return True
            # else Run Recursion
            else:
                self.right.contains(target)
        # Else Check Left
        else:
            # If None Return False
            if self.left == None:
                return False
            # elif left == target return true
            elif self.left.value == target:
                return True
            # else Run Recursion
            else:
                self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Steps
        # Create a var to hold current node position
        currentNode = self
        # Loop until the current node has no Right value
        while currentNode.right is not None:
            currentNode = currentNode.right

        return currentNode.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Steps:
        # Run FN on current node value
        fn(self.value)
        # If current node has a left value - Run Recurision
        if self.left:
            self.left.for_each(fn)
            # If current node has a right value - Run Recurision
        if self.right:
            self.right.for_each(fn)

        # Each time the function runs its going to only add the current node which moves
        # everytime it is ran recursively.

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
