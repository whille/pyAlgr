#!/usr/bin/env python
from nose.tools import assert_equal, assert_true, raises
import random
from sort import selection, insertion, shell, merge, mergeBU, quick, quick3way, heapsort


def test_all():
    _t(selection)
    _t(insertion)
    _t(shell)
    _t(merge)
    _t(mergeBU)
    _t(quick)
    _t(quick3way)
    _t(heapsort)


def _t(sort_fn):
    lst = [1, 4, 2, 3]
    sort_fn(lst)
    assert_equal([1, 2, 3, 4], lst)
    lst = [3]
    sort_fn(lst)
    assert_equal(lst, [3])
    lst = []
    sort_fn(lst)
    assert_equal(lst, [])
    lst = list(range(1000))
    random.shuffle(lst)
    sort_fn(lst)
    _assert_order(lst)
    lst = list("bdaecf")
    sort_fn(lst)
    assert_equal(list('abcdef'), lst)


def _assert_order(lst):
    for i in range(len(lst) - 1):
        assert_true(
            lst[i] <= lst[i + 1]), '%s: %s, %s' % (i, lst[i], lst[i + 1])
