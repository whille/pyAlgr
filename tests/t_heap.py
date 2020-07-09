#!/usr/bin/env python
from nose.tools import assert_equal, assert_true
from multiway_sort import multiway


class Stream:
    def __init__(self, start, end):
        self.lst = range(start, end)

    def readString(self):
        return self.lst.pop()

    def isEmpty(self):
        return not self.lst


def test_sort():
    streams = Stream(0, 6), Stream(2, 10), Stream(3, 11)
    for v in multiway(streams):
        print v
    assert_equal([1, 2, 3, 4], 'a')
