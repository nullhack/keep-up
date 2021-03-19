"""
Maximize value given weight in capacity
Bounded Knapsack problem (xi in [0,1,...,c]) -> dynamic programming, refactor loop order of 0/1

we would pick either the maximum value that we can obtain for any item i, at each max capacity
"""

def knapsack(values, weights, capacity):
    m = [0 for _ in range(capacity+1)]
    n = len(values)
    for w in range(1, capacity+1):
        m[w] = m[w-1]
        for i in range(n):
            if weights[i]<=w:
                m[w] = max(m[w], m[w-weights[i]]+values[i])
    return m


if __name__=="__main__":
    import numpy as np
    n = 5
    capacity = 5*n
    values = np.random.randint(1, 100, n)
    weights = np.random.randint(1, 100, n)

    s = zip(values, weights)
    s = sorted(s, key=lambda x: x[0]/x[1], reverse=True)
    r = knapsack(values, weights, capacity)
    n = len(r)
    print({i:r[i] for i in range(n)})
    print(s)
    print(capacity)

