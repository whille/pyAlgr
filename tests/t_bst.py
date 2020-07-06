#!/usr/bin/env python
from nose.tools import assert_equal, assert_true
from bst import BST
from rb_bst import RedBlackBST
from hash_st import LinearProbingHashST


def _test_bst(st):
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
        # print('key: %s: v: %s, rank: %s , select: %s' % (key, v, i, k))
    st.delete_min()
    assert_equal(keys[1], st.min())
    st.delete('M')


def test_bst():
    for St in BST, RedBlackBST:
        print St.__name__
        _test_bst(St())


def test_hashst():
    line = 'SEARCHEXAMPLE'
    st = LinearProbingHashST()
    dic_check = {}
    for i, key in enumerate(list(line)):
        dic_check[key] = i
        st.put(key, i)
    for k, v in dic_check.items():
        assert_equal(v, st.get(k))
