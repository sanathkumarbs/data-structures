#!/usr/bin/env python
import logging
from linkedlists.linkedlist import Node

logging.basicConfig(level=logging.DEBUG)

class TestNode(object):

    def test_one(self):
        """Test the Node class."""
        node = Node(10)

        assert(node.data==10)
        assert(node.next==None)

    def test_two(self):
        """Test multiple nodes."""
        n1 = Node(10)
        n2 = Node(20)
        n1.next = n2

        assert(n1.data==10)
        assert(n2.data==20)
        assert(n1.next==n2)


class TestLinkedList(object):

    def _create_sample_linkedlist(self):
        """Create a sample linkedlist of size four and return its head."""
        n1 = Node(10)
        n2 = Node(20)
        n1.next = n2

        n3 = Node(30)
        n2.next = n3

        n4 = Node(40)
        n3.next = n4

        return n1

    def test_one(self):
        """Testing traversing a linkedlist."""
        head = self._create_sample_linkedlist()
        cur = head
        count = 0
        
        while cur:
            count += 1
            logging.debug("Data is {0}".format(cur.data))
            cur = cur.next

        assert(count == 4)

    def test_two(self):
        """Testing inserting node at the head."""
        head = self._create_sample_linkedlist()

        node = Node(100)
        node.next = head
        head = node

        assert(head.data == 100)
        assert(head.next.data == 10)

        cur = head
        while cur:
            logging.debug("Data is {0}".format(cur.data))
            cur = cur.next