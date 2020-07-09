#!/usr/bin/env python
import random


# exchange i, j in list
def exch(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


# P248, O(N^2)
def selection(lst):
    for i in range(0, len(lst)):
        _min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[_min]:
                _min = j
        exch(lst, _min, i)  # move mininum to i


# P249, O(N^2), suitable for small list or partial order list
def _insertion(lst, lo, hi):
    for i in range(lo + 1, hi + 1):
        for j in range(i, lo, -1):  # backwards
            if lst[j] < lst[j - 1]:
                exch(lst, j, j - 1)
            else:
                break


def insertion(lst):
    _insertion(lst, 0, len(lst) - 1)


# P258, based on insertion, but increase switch step h, so called h-step order.
# advantage: simple to implement, no need extra space
def shell(lst):
    N = len(lst)
    h = 1
    while h < N // 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, N):
            for j in range(i, h - 1, -h):
                if lst[j] < lst[j - h]:
                    exch(lst, j, j - h)
                else:
                    break
        h = h / 3


# P271
def _merge(aux, lst, lo, mid, hi):
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        aux[k] = lst[k]
    for k in range(lo, hi + 1):
        if i > mid:
            lst[k] = aux[j]
            j += 1
        elif j > hi:
            lst[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            lst[k] = aux[j]
            j += 1
        else:
            lst[k] = aux[i]
            i += 1


# P271, O(Nlg(N))
def merge(lst):
    aux = [0] * len(lst)

    def _sort(lst, lo, hi):
        if hi <= lo:
            return
        mid = (lo + hi) // 2
        _sort(lst, lo, mid)
        _sort(lst, mid + 1, hi)
        if lst[mid] > lst[mid + 1]:  # P275
            _merge(aux, lst, lo, mid, hi)

    _sort(lst, 0, len(lst) - 1)


# P278, bottom up merge
def mergeBU(lst):
    N = len(lst)
    aux = [0] * N
    sz = 1
    while sz < N:
        for lo in range(0, N - sz, sz * 2):
            _merge(aux, lst, lo, lo + sz - 1, min(lo + 2 * sz - 1, N - 1))
        sz *= 2


# P291
def partition(lst, lo, hi):
    i, j = lo, hi + 1
    v = lst[lo]  # comparable value
    while True:
        i += 1
        j -= 1
        while lst[i] < v and i < hi:
            i += 1
        while v < lst[j] and j > lo:
            j -= 1
        if i >= j:
            break
        exch(lst, i, j)
    exch(lst, lo, j)
    return j


# P288
def quick(lst):
    M = 10

    def _sort(lst, lo, hi):
        # if hi <= lo: return
        if hi <= lo + M:  # inprovement, P295
            _insertion(lst, lo, hi)
            return
        j = partition(lst, lo, hi)
        _sort(lst, lo, j - 1)
        _sort(lst, j + 1, hi)

    random.shuffle(lst)
    _sort(lst, 0, len(lst) - 1)


def compare(x, y):
    res = 0
    if x < y:
        res = -1
    elif x > y:
        res = 1
    return res


# P298, suitable for mass repeated values
def quick3way(lst):

    def _sort(lst, lo, hi):
        if hi <= lo:
            return
        lt, i, gt = lo, lo + 1, hi
        v = lst[lo]
        while i <= gt:
            cmp = compare(lst[i], v)
            if cmp < 0:
                exch(lst, lt, i)
                lt += 1
                i += 1
            elif cmp > 0:
                exch(lst, i, gt)
                gt -= 1
            else:
                i += 1
        _sort(lst, lo, lt - 1)
        _sort(lst, gt + 1, hi)

    random.shuffle(lst)
    _sort(lst, 0, len(lst) - 1)


# max top
def sink(lst, k, N):
    while 2 * (k + 1) <= N + 1:
        j = 2 * k + 1
        if j < N and lst[j] < lst[j + 1]:
            j += 1
        if lst[k] >= lst[j]:
            break
        exch(lst, k, j)
        k = j


# P323
def heapsort(lst):
    N = len(lst) - 1
    for k in range((N + 1) // 2 - 1, -1, -1):
        sink(lst, k, N)
    while N > 0:
        exch(lst, 0, N)
        N -= 1
        sink(lst, 0, N)


# P346
def kth_min(lst, k):
    random.shuffle(lst)
    lo, hi = 0, len(lst) - 1
    while hi > lo:
        j = partition(lst, lo, hi)
        if j == k:
            return lst[k]
        elif j > k:
            hi = j - 1
        else:
            lo = j + 1
    return lst[k]
