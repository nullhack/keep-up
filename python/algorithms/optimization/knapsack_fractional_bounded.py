"""
the fractional can be solved with greedy algorithm
Maximize value picking the maximum value per weight available, as many units as possible
"""

def knapsack(values, weights, capacity, max_units):
    total_weight = 0
    total_value = 0
    chosen = []
    s = zip(values, weights)
    s = sorted(s, key=lambda x: x[0]/x[1], reverse=True)
    for value, weight in s:
        if total_weight<capacity:
            units = min(max_units, (capacity - total_weight)/weight)
            total_weight += weight*units
            total_value += value*units
            chosen.append((value, weight, units))
    return chosen, total_value


if __name__=="__main__":
    import numpy as np
    n = 5
    capacity = 20*n
    max_units = np.random.randint(1, 4)
    values = np.random.randint(1, 100, n)
    weights = np.random.randint(1, 100, n)

    s = zip(values, weights)
    s = sorted(s, key=lambda x: x[0]/x[1], reverse=True)
    print(s)
    print(max_units, capacity)
    print(knapsack(values, weights, capacity, max_units))
