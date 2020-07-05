#!/usr/bin/env python
from nose.tools import assert_equal, assert_true, raises
from utils import Link, Queue, Bag


def test_link():
    link = Link()
    link.push(3)
    link.push(2)
    assert_equal(2, link.size())
    assert_equal([2, 3], list(link))
    assert_equal(2, link.pop())
    assert_equal(1, link.size())


def test_queue():
    q = Queue()
    q.enqueue(3)
    assert_equal(1, q.size())
    assert_equal(3, q.dequeue())
    q.enqueue(2)
    q.enqueue(1)
    assert_equal([2, 1], list(q))
    assert_equal(2, q.dequeue())


def test_bag():
    b = Bag()
    b.add(3)
    assert_equal(1, b.size())
    b.add(2)
    assert_equal([2, 3], list(b))
