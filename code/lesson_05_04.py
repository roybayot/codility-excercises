"""
Div Count
"""

from math import floor, ceil

def solution(A, B, K):
    """
    50% solution. not okay for big ranges like 0-2M
    """
    AB_range = list(range(A, B + 1))
    count = 0
    for i in AB_range:
        if i % K == 0:
            count = count + 1
    return count


def solution2(A, B, K):
    """
    62%
    """
    min_fac = 0
    max_fac = 0

    for i in range(A, B + 1):
        if i % K == 0:
            min_fac = i // K
            break

    for i in range(B, A, -1):
        if i % K == 0:
            max_fac = i // K
            break

    return max_fac - min_fac + 1


def solution3(A, B, K):
    """

    """
    min_fac = 0
    max_fac = 0

    for i in range(A, B + 1):
        if i % K == 0:
            min_fac = i // K
            break

    for i in range(B, A, -1):
        if i % K == 0:
            max_fac = i // K
            break

    if A == 0 and B == 0:
        return 1
    elif min_fac == 0 and max_fac == 0:
        return 0
    else:
        return max_fac - min_fac + 1


def solution4(A, B, K):
    if A % K != 0:
        min_fac = A // K + 1
    else:
        min_fac = A // K

    if B % K != 0:
        max_fac = B // K - 1
    else:
        max_fac = B // K

    if A == 0:
        return max_fac - min_fac
    elif max_fac - min_fac + 1 < 0:
        return 1
    else:
        return max_fac - min_fac + 1


def solution(A, B, K):
    # write your code in Python 3.6
    """
    100%
    """
    start = ceil(A / K)
    end = floor(B / K)

    return end - start + 1
