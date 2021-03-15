"""
Choose a pivot, split the elements in between smaller/bigger than the pivot, repeat
"""

class QuickSort:
    def __init__(self, l):
        self.l = l.copy()
        self.n = len(l)

    def solve(self):
        self._solve(0, self.n - 1)

    def _solve(self, i=0, j=None):
        if j is None:
            j = self.n - 1
        if i < j:
            lb = self.l[i]
            up = self.l[j]
            mb = self.l[(i + j) // 2]
            m = (lb + up + mb) / 3
            ri = i
            li = j
            while ri < li:
                if self.l[ri] < m:
                    ri += 1
                else:
                    self.l[ri], self.l[li] = self.l[li], self.l[ri]
                    li -= 1
            self._solve(i, ri - 1)
            self._solve(ri + 1, j)


if __name__ == "__main__":
    import numpy as np

    l = np.random.randint(0, 100, 100)
    q = QuickSort(l)
    q.solve()
    print(l)
    print(q.l)
