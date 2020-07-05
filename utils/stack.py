#!/usr/bin/env python


class Stack(object):

    def __init__(self):
        self.lst = []

    def push(self, v):
        self.lst.append(v)

    def pop(self):
        return self.lst.pop()


class ResizingArrayStack(object):
    def __init__(self):
        self.lst = [None]
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def resize(self, maxn):
        temp = [None, ] * maxn
        for i, v in enumerate(self.lst):
            temp[i] = v
        self.lst = temp

    def push(self, v):
        if self.N == len(self.lst):
            self.resize(2 * self.N)
        self.lst[self.N] = v
        self.N += 1

    def pop(self):
        self.N -= 1
        res = self.lst[self.N]
        self.lst[self.N] = None
        if self.N > 0 and self.N == len(self.lst) // 4:
            self.resize(len(self.lst) // 2)
        return res
