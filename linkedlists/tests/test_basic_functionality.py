#!/usr/bin/env python
import logging
from linkedlists.linkedlist import Node
from linkedlists.linkedlist import LinkedList

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

    def _get_sample_linkedlist(self, size = 4):
        """Create a sample linkedlist and return the linkedlist obj"""
        ll = LinkedList()

        for item in range(size):
            ll.push(item)
        
        return ll

    def test_one(self, size = 4):
        """Testing traversing a linkedlist."""
        ll = self._get_sample_linkedlist(size)
        cur = ll.head
        count = 0
        
        while cur:
            count += 1
            logging.debug("Data is {0}".format(cur.data))
            cur = cur.next

        assert(count == 4)

    def test_two(self, data = 20):
        """Testing inserting node at the head."""
        ll = self._get_sample_linkedlist()
        ll.push(data, 0)
        
        logging.debug("Data is {0}".format(ll.head.data))
        assert(ll.head.data == data)

    def test_three(self, size = 4):
        """Testing get on linkedlist."""
        ll = self._get_sample_linkedlist(size)
        assert(ll.get(index = 1).data == 1)

    def test_four(self, index = 2, data = 50):
        """Testing inseting node at nth position."""
        ll = self._get_sample_linkedlist(size = 10)
        ll.push(data, index)
        assert(ll.get(index).data == data)

    def test_five(self):
        """Testing deleting head node."""
        ll = self._get_sample_linkedlist()
        logging.debug("Data is {0}".format(ll.head.data))

        ll.pop(0)
        logging.debug("Data is {0}".format(ll.head.data))
        assert(ll.head.data == 1)

    def test_six(self):
        """Testing deleting the last node."""
        ll = self._get_sample_linkedlist()
        last = ll.length() - 1
        logging.debug("Data is {0}".format(ll.get(last).data))

        ll.pop(last)

        last = ll.length() - 1
        logging.debug("Data is {0}".format(ll.get(last).data))
        assert(ll.get(last).data == 2)

    def test_seven(self, index = 2):
        """Testing deleting a nth node."""
        ll = self._get_sample_linkedlist()
        logging.debug("Data is {0}".format(ll.get(index).data))

        ll.pop(index)
        logging.debug("Data is {0}".format(ll.get(index).data))
        assert(ll.get(index).data == 3)