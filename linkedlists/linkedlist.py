#!/usr/bin/env python
"""LinkedIn Implementation."""

class Node(object):
    """Implementation of a Node of a linkedlist."""

    def __init__(self, data, next = None):
        """Initialize a node with data and next pointer."""
        self.data = data
        self.next = next

class LinkedList(object):
    """Implementation of a 0th indexed linkedlist."""

    def __init__(self, head = None):
        """Initialize a linkedlist with a head."""
        self.head = head

    def length(self):
        """Get the length of the linkedlist."""
        items = 0
        if self.head:
            cur = self.head

            while cur:
                items += 1
                cur = cur.next

        return items

    def pprint(self):
        """Print all the elements of the linkedlist."""
        cur = self.head
        l = []
        while cur:
            l.append(cur.data)
            cur = cur.next
        print l

    def get(self, index):
        """Get the index node from linkedlist"""
        cur = self.head
        for _ in range(0, index):
            cur = cur.next
        return cur

    def push(self, data, index = None):
        """Push a node to the linkedlist at a given index."""
        node = Node(data)

        if index is not None: 
            if index == 0 and not self.head:
                self.head = node   
            elif index == 0 and self.head:
                node.next = self.head
                self.head = node
            elif index <= self.length() and index >= 0 and self.head:
                cur = self.head
                
                for _ in range(0, index-1):
                    cur = cur.next
                
                temp = cur.next
                cur.next = node
                node.next = temp
            else:
                raise KeyError("Invalid index. Expected {0} to {1}".format(0, self.length()))
        else:
            if self.head:
                cur = self.head
                while cur.next:
                    cur = cur.next
                cur.next = node
            else:
                self.head = node
    