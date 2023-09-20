# weighted edge
class BaseEdge(object):
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight


class Edge(BaseEdge):
    def either(self):
        return self.v

    def other(self, v):
        if v == self.v:
            return self.w
        elif v == self.w:
            return self.v
        else:
            raise Exception("invalid edge")

    def __str__(self):
        return "%d-%s %.2f" % (self.v, self.w, self.weight)


# directed weighted edge
class DirectedEdge(BaseEdge):
    def From(self):
        return self.v

    def To(self):
        return self.w

    def __str__(self):
        return "%d->%s %.2f" % (self.v, self.w, self.weight)
