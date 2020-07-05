#!/usr/bin/env python
from nose.tools import assert_equal, assert_true, raises
from union_find import UF, QuickUnion, WeightedQuickUnion


def _t_uf(cls):
    uf = cls(10)
    txt = """
    0,1
    1,3
    3,5
    2,4
    4,8
    8,9
    6,7
    """
    for line in txt.split('\n'):
        line = line.strip()
        if not line:
            continue
        p, q = line.split(',')
        uf.union(int(p), int(q))
    assert_true(uf.connected(1, 5))
    assert_equal(3, uf.count)
#     for i, v in enumerate(uf.id):
#         print i, uf.find(v)


def test_ufs():
    for cls in (UF, QuickUnion, WeightedQuickUnion):
        _t_uf(cls)

