from bst import BST

RED = True
BLACK = False


class RBNode:
    def __init__(self, key, v, N, color):
        self.key = key
        self.v = v
        self.left = None
        self.right = None
        self.N = N
        self.color = color      # from parent link's color


class RedBlackBST(BST):
    def is_red(self, x):
        if x is None:
            return BLACK
        return x.color == RED

    def put(self, key, v):
        self.root = self._put(self.root, key, v)
        self.root.color = BLACK

    def _put(self, x, key, v):
        if x is None:
            return RBNode(key, v, RED, 1)
        if key < x.key:
            x.left = self._put(x.left, key, v)
        elif key > x.key:
            x.right = self._put(x.right, key, v)
        else:
            x.v = v

        # fix-up any right-leaning links
        if self.is_red(x.right) and not self.is_red(x.left):
            x = self.rotate_left(x)
        if self.is_red(x.left) and self.is_red(x.left.left):
            x = self.rotate_right(x)
        if self.is_red(x.left) and self.is_red(x.right):
            self.flip_colors(x)
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    # P434
    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self._size(h.left) + self._size(h.right)
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self._size(h.left) + self._size(h.right)
        return x

    def flip_colors(self, h):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def move_red_left(self, h):
        """
        Assuming that h is red and both h.left and h.left.left
        are black, make h.left or one of its children red.
        """
        self.flip_colors(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h

    def move_red_right(self, h):
        """
        Assuming that h is red and both h.right and h.right.left
        are black, make h.right or one of its children red.
        """
        self.flip_colors(h)
        if self.is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h

    def delete(self, key):
        if key is None:
            raise ValueError("argument is null")
        # if both children of root are black, set root to red
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RED
        self.root = self._delete(self.root, key)
        if not self.is_empty():
            self.root.color = BLACK

    def _delete(self, h, key):
        if key < h.key:
            if not self.is_red(h.left) and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            if key == h.key and h.right is None:
                return None
            if not self.is_red(h.right) and not self.is_red(h.right.left):
                h = self.move_red_right(h)
            if key == h.key:
                x = self._min(h.right)
                h.key = x.key
                h.v = x.v
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)
        return self.balance(h)

    def delete_min(self):
        if self.is_empty():
            raise ValueError("BST underflow")
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RED
        self.root = self._delete_min(self.root)
        if not self.is_empty():
            self.root.color = BLACK

    def _delete_min(self, h):
        if h.left is None:
            return None
        if not self.is_red(h.left) and not self.is_red(h.left.left):
            h = self.move_red_left(h)
        h.left = self._delete_min(h.left)
        return self.balance(h)

    def balance(self, h):
        if self.is_red(h.right):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        h.N = self._size(h.left) + self._size(h.right) + 1
        return h
