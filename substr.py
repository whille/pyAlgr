#!/usr/bin/env python


def test():
    for pat, txt in (
        ('ABABC', 'ABABABC'),
        ('ABC', 'DABABCABC'),
        ('XBC', 'DABABCABC'),
    ):
        show(pat, txt)


def show(pat, txt):
    pos = search(txt, pat)
    print txt, pos
    if pos <= len(txt) - len(pat):
        substr = txt[pos:pos + len(pat)]
        print '%s%s%s' % (' ' * pos, substr, txt[pos + len(pat):])
        assert pat == substr, substr
    else:
        print 'no substring for', pat


def search(txt, pat):
    right = {}
    for i, c in enumerate(pat):
        right[c] = i
    # print 'right:', right
    M, N = len(pat), len(txt)
    i = 0
    while i <= N - M:
        for j in range(M - 1, -1, -1):
            if txt[i + j] != pat[j]:
                i += j - (right.get(txt[i + j], -1))
                break
        else:
            return i
    return i
