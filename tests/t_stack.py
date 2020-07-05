#!/usr/bin/env python
from nose.tools import assert_equal, assert_true, raises
from utils import ResizingArrayStack


def test_resizestack():
    st = ResizingArrayStack()
    st.push(1)
    assert_equal(1, st.size())
    st.push(3)
    assert_equal(3, st.pop())
