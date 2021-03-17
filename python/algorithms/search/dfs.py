class BinaryTree:
    def __init__(self, l=[]):
        self.l = l
        self.n = len(l) - 1

    @staticmethod
    def _parent_index(n):
        return (n - 1) // 2

    @staticmethod
    def _left_child_index(n):
        return 2 * n + 1

    @staticmethod
    def _right_child_index(n):
        return 2 * n + 2

    def insert(self, e):
        self.l.append(e)
        self.n += 1

    def dfs(self, n, i = 0):
        if i>=0 and i<=self.n:
            s = self.l[i]
            print(i, s)
            if s==n:
                return True
            else:
                v = self.dfs(n, self._left_child_index(i))
                if not v:
                    v = self.dfs(n, self._right_child_index(i))
                if not v:
                    return False

if __name__ == "__main__":
    import numpy as np

    l = np.random.randint(0, 20, 20)
    b = BinaryTree(l)
    print(l)
    b.dfs(5)
