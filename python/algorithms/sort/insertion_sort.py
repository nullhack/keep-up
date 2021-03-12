class InsertionSort:
    def __init__(self, l):
        self.l = l.copy()
        self.n = len(l)

    def solve(self):
        for m in range(1, self.n):
            n = m
            while n > 0 and self.l[n - 1] > self.l[n]:
                self.l[n - 1], self.l[n] = self.l[n], self.l[n - 1]
                n -= 1


if __name__ == "__main__":
    import numpy as np

    l = np.random.randint(0, 100, 100)
    q = InsertionSort(l)
    q.solve()
    print(l)
    print(q.l)
