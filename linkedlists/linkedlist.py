#!/usr/bin/env python
"""LinkedIn Implementation."""

class Node(object):
    """Implementation of a Node of a linkedlist."""

    def __init__(self, data, next = None):
        """Initialize a node with data and next pointer."""
        self.data = data
        self.next = next


class DoubleNode(object):
    """Implementation of a Node of a doubly linkedlist."""

    def __init__(self, data, prev = None, next = None):
        """Initialize a node with data, prev and next pointers."""
        self.data = data
        self.prev = prev
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

    def pop(self, index = None):
        """Pop a node from the linkedlist."""
        if index is not None:
            if index == 0 and self.head:
                self.head = self.head.next
            elif index > 0 and index < self.length() and self.head:
                cur = self.head

                for _ in range(0, index - 1):
                    cur = cur.next
                
                cur.next = cur.next.next
            else:
                raise KeyError("Invalid index. Expected {0} to {1}".format(0, self.length()))
        else:
            cur = self.head
            
            while cur.next.next is not None:
                cur = cur.next
            
            cur.next = None


class DoublyLinkedList(LinkedList):
    """Implementation of a 0th indexed doubly linkedlist."""

    def __init__(self, head = None):
        LinkedList.__init__(self, head)

    def push(self, data, index = None):
        doublenode = DoubleNode(data)

        if index is not None:
            # push at the index
            if index == 0 and self.head:
                # insert at the head
                # head node exists
                doublenode.next = self.head
                self.head.prev = doublenode
                self.head = doublenode
            elif index == 0 and not self.head:
                # insert at the head
                # head node doesn't exist
                self.head = doublenode
            elif index > 0 and index <= self.length() and self.head:
                # insert at the index
                # head node exists
                cur = self.head
                prev = self.head.prev

                for _ in range(0, index):
                    prev = cur
                    cur = cur.next

                prev.next = doublenode
                doublenode.prev = prev

                doublenode.next = cur
                cur.prev = doublenode
            else:
                raise KeyError("Invalid index. Expected {0} to {1}".format(0, self.length()))
        else:
            # push at the end
            if self.head:
                # head node exists
                cur = self.head
                prev = self.head.prev

                while cur is not None:
                    prev = cur
                    cur = cur.next    

                prev.next = doublenode
                doublenode.prev = prev
            else:
                # create head node
                self.head = doublenode

    def pop(self, index = Node):
        if index is not None:
            # remove the index node
            if index == 0 and self.head:
                # remove the head 
                self.head = self.head.next
                self.head.prev = None
            elif index > 0 and index < self.length() and self.head:
                # remove the index node
                cur = self.head
                prev = self.head.prev

                for _ in range(0, index):
                    prev = cur
                    cur = cur.next

                prev.next = cur.next
                if cur.next:
                    cur.next.prev = prev
        else:
            # remove the last node
            if self.head:
                # head exists
                cur = self.head
                prev = self.head.prev

                while cur is not None:
                    prev = cur
                    cur = cur.next

                prev.prev.next = None
    