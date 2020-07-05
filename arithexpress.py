#!/usr/bin/env python
# P 129, Dijkstra's double stack algrithm for arithmetic expression


class Stack(object):

    def __init__(self):
        self.lst = []

    def push(self, v):
        self.lst.append(v)

    def pop(self):
        return self.lst.pop()


def evaluate(express):
    ops = Stack()
    vals = Stack()
    for s in express.split():
        if s in "+,-,*,/,sqrt".split(','):
            ops.push(s)
        elif s == '(':
            pass
        elif s == ')':
            op = ops.pop()
            v = vals.pop()
            if op == '+':
                v += vals.pop()
            elif op == '-':
                v -= vals.pop()
            elif op == '*':
                v *= vals.pop()
            elif op == '/':
                v /= vals.pop()
            elif op == 'sqrt':
                v = v**0.5
            vals.push(v)
        else:
            vals.push(float(s))
    return vals.pop()


def gen_stdin():
    import fileinput
    for line in fileinput.input():
        line = line.rstrip()
        if not line:
            break
        else:
            yield line


if __name__ == "__main__":
    for express in gen_stdin():
        print evaluate(express)
