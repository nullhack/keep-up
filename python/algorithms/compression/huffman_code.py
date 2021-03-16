"""
Group worst elements together as leaves of a tree, then repeat until no more groups/elements to group
"""

class Node:
    def __init__(self, rep="", value=0, l=None, r=None):
        self.rep = rep
        self.value = value
        self.l = l
        self.r = r

class Huffman:
    def __init__(self, a, l):
        if len(a)!=len(l):
            raise Exception("size of lists don't match")
        self.a = a
        self.l = l
        self.sol = Node()

    def solve(self):
        sl = [Node(r, v) for r,v in zip(self.a, self.l)]
        while len(sl)>=2:
            sl = sorted(sl, key=lambda x:x.value)
            x = sl.pop(0)
            y = sl.pop(0)
            n = Node(x.rep+y.rep, x.value+y.value, x, y)
            sl.append(n)
        self.sol = sl.pop(0)

    def print_sol(self, node=None, symbol=""):
        if node is None:
            node = self.sol

        if node.l is None and node.r is None:
            print(node.rep, symbol)
        else:
            if node.l:
                self.print_sol(node.l, symbol+"0")
            if node.r:
                self.print_sol(node.r, symbol+"1")


if __name__=="__main__":
    import numpy as np

    a = "abcdefghijkllmnopqrstuvwyxz"
    l = np.random.randint(0, 100, len(a))
    h = Huffman(a, l)
    h.solve()
    h.print_sol()
