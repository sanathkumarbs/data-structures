#!/usr/bin/env python
"""LinkedIn Implementation."""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next