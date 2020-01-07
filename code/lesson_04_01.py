"""
PermCheck
"""


def counting(A, m):
    """
    A gives the list.
    m is the number of integers in the list from zero
    """

    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count


def solution2(A):
    # write your code in Python 3.6
    A.sort()

    if len(A) == 0:
        return 0
    elif len(A) == 1 and A[0] != 1:
        return 0
    else:
        count = counting(A, A[-1])
        if sum(count[1:]) == len(count) - 1:
            return 1
        else:
            return 0

# solution 2. if you have [1000000000], it terminates


def solution3(A):
    """
    100% codility
    """
    A.sort()
    if A[0] == 1 and A[-1] == len(A):
        count = counting(A, A[-1])
        if sum(count[1:]) == len(count) - 1:
            for x in count[1:]:
                if x != 1:
                    return 0
            return 1
        else:
            return 0
    else:
        return 0


def count(A, item):
    one_count = [1 for a in A if a == item]
    return sum(one_count)


def solution(A):
    is_permutation = False
    items = list(range(1, len(A) + 1))

    counts_per_item = [count(A, item) for item in items]
    list_unique_counts = list(set(counts_per_item))

    if len(list_unique_counts) == 1 and list_unique_counts[0] == 1:
        return 1  # it is a permutation
    else:
        return 0
