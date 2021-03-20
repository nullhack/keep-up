"""
given array of integers, find the largest sum subarray

idea 1: keep track of positive subsums and return the biggest
idea 2: keep track of start and end of max
"""

def lscs(l):
    n = len(l)
    s = ms = 0
    e = me = 0
    m = mm = l[0]
    for i in range(1, n):
        if m >= 0:
            m = l[i] + m
            e = i
        else:
            s = i
            e = i
            m = l[i]

        if m>mm:
            mm = m
            ms = s
            me = e

    return l[ms:me+1]

if __name__=="__main__":
    import numpy as np
    r = list(np.random.randint(-10, 15, 10))
    arr = lscs(r)
    print(r)
    print(arr, sum(arr))
