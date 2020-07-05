#!/usr/bin/env python


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
def insertion(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):  # backwards
            if lst[j] < lst[j - 1]:
                exch(lst, j, j - 1)
            else:
                break


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


# bottom up merge # 278
def mergeBU(lst):
    N = len(lst)
    aux = [0] * N
    sz = 1
    while sz < N:
        for lo in range(0, N - sz, sz * 2):
            _merge(aux, lst, lo, lo + sz - 1, min(lo + 2 * sz - 1, N - 1))
        sz *= 2
