#!/usr/bin/env python


class Node(object):
    def __init__(self, v, Next=None):
        self.v = v
        self.next = Next


class Container(object):
    def __init__(self):
        self.first = None
        self.N = 0

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.N

    def __iter__(self):
        p = self.first
        while p:
            yield p.v
            p = p.next


# P155
class Bag(Container):
    def add(self, v):
        oldfirst = self.first
        self.first = Node(v, oldfirst)
        self.N += 1


# P147
class Link(Container):
    def push(self, v):
        oldfirst = self.first
        self.first = Node(v, oldfirst)
        self.N += 1

    def pop(self):
        v = self.first.v
        self.first = self.first.next
        self.N -= 1
        return v


# P150
class Queue(Container):
    def __init__(self):
        self.first = None
        self.last = None
        self.N = 0

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.N

    def enqueue(self, v):
        n = Node(v)
        if self.isEmpty():
            self.first = n
        else:
            self.last.next = n
        self.last = n
        self.N += 1

    def dequeue(self):
        v = self.first.v
        self.first = self.first.next
        if self.isEmpty():
            self.last = None
        self.N -= 1
        return v
