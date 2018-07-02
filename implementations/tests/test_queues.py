#!/usr/bin/env python
"""Unit tests for queues implementation."""
import logging
from implementations.lib.queues import ArrayQueue, LinkedListQueue

logging.basicConfig(level=logging.DEBUG)

class TestArrayQueues(object):
    """Test class to test ArrayQueue class."""

    def test_one(self):
        """Test isempty()."""
        queue = ArrayQueue()
        assert(queue.isempty is True)
    
    def test_two(self):
        """Test pushing an element to queue."""
        queue = ArrayQueue()
        queue.enqueue(10)

        assert(queue.isempty is False)
        assert(queue.front == 10)

    def test_three(self):
        """Test popping an element from queue."""
        queue = ArrayQueue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.dequeue()

        assert(queue.isempty is False)
        assert(queue.front == 20)

class TestLinkedListQueues(object):
    """Test class to test LinkedListQueue class."""

    def test_one(self):
        """Test isempty()."""
        queue = LinkedListQueue()
        assert(queue.isempty is True)
    
    def test_two(self):
        """Test pushing an element to queue."""
        queue = LinkedListQueue()
        queue.enqueue(10)

        assert(queue.isempty is False)
        assert(queue.front == 10)

    def test_three(self):
        """Test popping an element from queue."""
        queue = LinkedListQueue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.dequeue()

        assert(queue.isempty is False)
        assert(queue.front == 20)