#!/usr/bin/env python
from nose.tools import assert_equal, assert_true, raises

from arithexpress import evaluate


def test_express():
    for express, res in (
        ("( 1 + 100 )", 101),
        ("( 1 + ( 5 * 20 ) )", 101),
        ("( 1 + ( 5 * ( 4 * 5 ) ) )", 101),


    ):
        assert_equal(evaluate(express), res)
