#!/usr/bin/env python
from nose.tools import assert_equal, assert_true
from bst import BST


def test_bst():
    st = BST()
    i = 0
    # https://algs4.cs.princeton.edu/32bst/tinyST.txt
    line = 'SEARCHEXAMPLE'
    dic_check = {}
    for i, key in enumerate(list(line)):
        dic_check[key] = i
        st.put(key, i)
    keys = st.keys()
    for i in range(len(keys) - 1):
        assert_true(keys[i] <= keys[i + 1])
        assert_true(st.rank(keys[i]) <= st.rank(keys[i + 1]))
    for key in keys:
        v = st.get(key)
        i = st.rank(key)
        k = st.select(i)
        assert_equal(v, dic_check[key])
        assert_equal(k, key)
        print('key: %s: v: %s, rank: %s , select: %s' % (key, v, i, k))
