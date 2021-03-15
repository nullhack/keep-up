"""
Adding/removing a new element to a heap can be done in O(log(n))
Heap is a binary tree in which the parent is always bigger/smaller (max/min heap) than It's childs
"""

class MinHeap:
    def __init__(self):
        self.l = []
        self.n = -1

    @staticmethod
    def _parent_index(n):
        return (n - 1) // 2

    @staticmethod
    def _left_child_index(n):
        return 2 * n + 1

    @staticmethod
    def _right_child_index(n):
        return 2 * n + 2

    def _min_child_index(self, n):
        left = self._left_child_index(n)
        right = self._right_child_index(n)
        r = right
        if self.l[left] < self.l[right]:
            r = left
        return r

    def _switch(self, i, j):
        self.l[i], self.l[j] = self.l[j], self.l[i]

    def insert(self, e):
        self.l.append(e)
        self.n += 1
        i = self.n
        while i > 0 and self.l[i] < self.l[self._parent_index(i)]:
            self._switch(i, self._parent_index(i))
            i = self._parent_index(i)

    def extract(self):
        if not self.l:
            return []

        self._switch(0, self.n)
        r = self.l.pop()
        i = 0
        while (
            i < self._parent_index(self.n)
            and self.l[i] > self.l[self._min_child_index(i)]
        ):
            mci = self._min_child_index(i)
            self._switch(i, mci)
            i = mci
        self.n -= 1
        return r


class HeapSort:
    def __init__(self, l):
        self.l = list(l.copy())
        self.n = len(l)

    def solve(self):
        h = MinHeap()

        for i in self.l:
            h.insert(i)

        for i in range(self.n):
            self.l[i] = h.extract()


if __name__ == "__main__":
    import numpy as np

    l = np.random.randint(0, 100, 100)
    q = HeapSort(l)
    q.solve()
    print(l)
    print(q.l)
