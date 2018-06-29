#!/usr/bin/env python
"""Stacks Implementation."""

from linkedlist import LinkedList

class ArrayStack(object):
    """Implementation of Stacks using Arrays."""

    def __init__(self):
        """Initialize the Stack."""
        self.stack = []

    @property
    def isempty(self):
        """Check if the stack is empty."""
        if len(self.stack) > 0:
            return False
        return True

    @property
    def top(self):
        """Return the top item in the stack."""
        if self.isempty:
            return None
        return self.stack[-1]

    def push(self, item):
        """Push an item at the top of stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item at the top of stack."""
        self.stack.pop()


class LinkedListStack(object):
    """Implementation of Stacks using LinkedList."""

    def __init__(self):
        """Initialize the Stack."""
        self.stack = LinkedList()

    @property
    def isempty(self):
        """Check if the stack is empty."""
        if self.stack.length() > 0:
            return False
        return True

    @property
    def top(self):
        """Return the top item in the stack."""
        if self.isempty:
            return None
        return self.stack.head.data

    def push(self, item):
        """Push an item at the top of stack."""
        self.stack.push(item, index=0)

    def pop(self):
        """Pop an item at the top of stack."""
        self.stack.pop(index=0)


