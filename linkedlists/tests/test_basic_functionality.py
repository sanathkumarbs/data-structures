#!/usr/bin/env python
import logging
from linkedlists.linkedlist import Node
from linkedlists.linkedlist import LinkedList, DoublyLinkedList

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
        assert(ll.head.next.data == 0)

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


class TestDoublyLinkedList(object):

    def _get_sample_linkedlist(self, size = 4):
        """Create a sample linkedlist and return the doubly linkedlist obj"""
        ll = DoublyLinkedList()

        for item in range(size):
            ll.push(item)
        
        return ll

    def test_one(self, size = 4):
        """Testing traversing a doubly linkedlist (forward)."""
        ll = self._get_sample_linkedlist(size)
        cur = ll.head
        count = 0
        
        while cur:
            count += 1
            logging.debug("Data is {0}".format(cur.data))
            cur = cur.next

        assert(count == 4)

    def test_two(self, size = 4):
        """Testing traversing a doubly linkedlist (backward)."""
        ll = self._get_sample_linkedlist(size)

        cur = ll.head
        prev = ll.head.prev

        count = 0
        
        while cur:
            count += 1
            logging.debug("Data is {0}".format(cur.data))
            prev = cur
            cur = cur.next
        
        cur = prev

        while cur:
            count -= 1
            logging.debug("Data is {0}".format(cur.data))
            cur = cur.prev

        assert(count == 0)
    
    def test_three(self, data = 20):
        """Testing inserting node at the head."""
        ll = self._get_sample_linkedlist()
        ll.push(data, 0)
        
        logging.debug("Data is {0}".format(ll.head.data))
        assert(ll.head.data == data)
        assert(ll.head.next.data == 0)
        assert(ll.head.next.prev.data == data)
        assert(ll.head.prev == None)

    def test_four(self, size = 4):
        """Testing get on linkedlist."""
        ll = self._get_sample_linkedlist(size)
        assert(ll.get(index = 1).data == 1)

    def test_five(self, index = 2, data = 50):
        """Testing inseting node at nth position."""
        ll = self._get_sample_linkedlist(size = 10)
        
        nextval = ll.get(index).data
        prevval = ll.get(index-1).data

        ll.push(data, index)

        assert(ll.get(index).data == data)
        assert(ll.get(index).next.data == nextval)
        assert(ll.get(index).next.prev.data == data)
        assert(ll.get(index).prev.data == prevval)

    def test_six(self):
        """Testing deleting head node."""
        ll = self._get_sample_linkedlist()
        logging.debug("Data is {0}".format(ll.head.data))

        ll.pop(0)
        logging.debug("Data is {0}".format(ll.head.data))
        assert(ll.head.data == 1)
        assert(ll.head.prev == None)
        assert(ll.head.next.data == 2)
        assert(ll.head.next.prev.data == 1)

    def test_seven(self):
        """Testing deleting the last node."""
        ll = self._get_sample_linkedlist()
        last = ll.length() - 1
        logging.debug("Data is {0}".format(ll.get(last).data))

        ll.pop(last)
        last = ll.length() - 1
        logging.debug("Data is {0}".format(ll.get(last).data))
 
        assert(ll.get(last).data == 2)

    def test_eight(self, index = 1):
        """Testing deleting a nth node."""
        ll = self._get_sample_linkedlist()
        logging.debug("Data is {0}".format(ll.get(index).data))

        nextval = ll.get(index + 1).next.data
        prevval = ll.get(index - 1).data

        ll.pop(index)
        logging.debug("Data is {0}".format(ll.get(index).data))

        assert(ll.get(index).data == 2)
        assert(ll.get(index).next.data == nextval)
        assert(ll.get(index).prev.data == prevval)
        assert(ll.get(index).next.prev.data == 2)
