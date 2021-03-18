"""
the fractional can be solved with greedy algorithm
Maximize value given weight in capacity, and fill all the capacity with the item
"""

def knapsack(values, weights, capacity):
    total_value = 0
    chosen = []
    s = zip(values, weights)
    m = max(sorted(s, key=lambda x: x[0]/x[1], reverse=True))
    total_units = capacity/m[1]
    return m, total_units, total_units*m[0]


if __name__=="__main__":
    import numpy as np
    n = 5
    capacity = 20*n
    values = np.random.randint(1, 100, n)
    weights = np.random.randint(1, 100, n)

    s = zip(values, weights)
    s = sorted(s, key=lambda x: x[0]/x[1], reverse=True)
    print(s)
    print(capacity)
    print(knapsack(values, weights, capacity))
