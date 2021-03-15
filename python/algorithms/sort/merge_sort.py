"""
Merging two sorted linked lists can be done in O(n)
Dividing and conquering T(n) = 2T(n/2) + O(n) is in O(nlog(n)) by Master's theorem
"""

class MergeSort:
    def __init__(self, l):
        self.l = list(l.copy())

    @staticmethod
    def merge(a, b):
        l = []
        while a and b:
            if a[0] <= b[0]:
                l.append(a.pop(0))
            else:
                l.append(b.pop(0))
        return l + a + b

    def solve(self):
        self.l = self._solve(self.l)

    def _solve(self, l):
        if len(l) == 1:
            return l
        m = len(l) // 2
        a = self._solve(l[:m])
        b = self._solve(l[m:])
        return self.merge(a, b)


if __name__ == "__main__":
    import numpy as np

    l = np.random.randint(0, 100, 100)
    q = MergeSort(l)
    q.solve()
    print(l)
    print(q.l)
