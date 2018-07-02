#!/usr/bin/env python
"""Queues Implementation."""

from linkedlist import LinkedList

class ArrayQueue(object):
    """Implementation of Queues using Arrays."""

    def __init__(self):
        """Initialize the Queue."""
        self._queue = []

    @property
    def isempty(self):
        """Check if the queue is empty."""
        if len(self._queue) == 0:
            return True
        return False

    @property
    def front(self):
        """Return the front item in the queue."""
        return self._queue[-1]

    def enqueue(self, item):
        """Push an item at the tail of queue."""
        self._queue.insert(0, item)

    def dequeue(self):
        """Pop an item at the front of queue."""
        self._queue.pop()


class LinkedListQueue(object):
    """Implementation of Queues using LinkedList."""

    def __init__(self):
        """Initialize the Queue."""
        self._queue = LinkedList()

    @property
    def isempty(self):
        """Check if the queue is empty."""
        if self._queue.length() == 0:
            return True
        return False

    @property
    def front(self):
        """Return the front item in the queue."""
        if self._queue.head:
            return self._queue.head.data
        return None

    def enqueue(self, item):
        """Push an item at the tail of queue."""
        self._queue.push(item, index=0)

    def dequeue(self):
        """Pop an item at the front of queue."""
        self._queue.pop()