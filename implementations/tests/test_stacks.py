#!/usr/bin/env python
"""Unit tests for stacks implementation."""
import logging
from implementations.lib.stacks import ArrayStack, LinkedListStack

logging.basicConfig(level=logging.DEBUG)

class TestArrayStacks(object):
    """Test class to test ArrayStack class."""

    def test_one(self):
        """Test isempty()."""
        stack = ArrayStack()
        assert(stack.isempty is True)
    
    def test_two(self):
        """Test pushing an element to stack."""
        stack = ArrayStack()
        stack.push(10)

        assert(stack.isempty is False)
        assert(stack.top == 10)

    def test_three(self):
        """Test popping an element from stack."""
        stack = ArrayStack()
        stack.push(10)
        stack.push(20)
        stack.pop()

        assert(stack.isempty is False)
        assert(stack.top == 10)

class TestLinkedListStack(object):
    """Test class to test LinkedListStack class."""

    def test_one(self):
        """Test isempty()."""
        stack = LinkedListStack()
        assert(stack.isempty is True)
    
    def test_two(self):
        """Test pushing an element to stack."""
        stack = LinkedListStack()
        stack.push(10)

        assert(stack.isempty is False)
        assert(stack.top == 10)

    def test_three(self):
        """Test popping an element from stack."""
        stack = LinkedListStack()
        stack.push(10)
        stack.push(20)
        stack.pop()

        assert(stack.isempty is False)
        assert(stack.top == 10)