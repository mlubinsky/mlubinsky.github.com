# Python program to randomly select a node from singly
# linked list

import random

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data= data
        self.next = None

class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # A reservoir sampling based function to print a
    # random node from a linkd list
    def printRandom(self):

        # If list is empty
        if self.head is None:
            return

        # Use a different seed value so that we don't get
        # same result each time we run this program
        random.seed()

        # Initialize result as first node
        result = self.head.data

        # Iterate from the (k+1)th element nth element
        current = self.head
        n = 2
        while(current is not None):

            # change result with probability 1/n
            if (random.randrange(n) == 0 ):
                result = current.data

            # Move to next node
            current = current.next
            n += 1

        print "Randomly selected key is %d" %(result)

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next


# Driver program to test above function
llist = LinkedList()
llist.push(5)
llist.push(20)
llist.push(4)
llist.push(3)
llist.push(30)
llist.printRandom()