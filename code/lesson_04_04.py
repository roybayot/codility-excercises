"""
Missing Integer
"""


def solution(A):
    """
    22%
    """
    elems_of_A = set(A)
    list_elems_of_A = list(elems_of_A)
    list_elems_of_A.sort()
    min_elem = list_elems_of_A[0]
    max_elem = list_elems_of_A[-1]

    elems_needed = set(range(min_elem, max_elem + 1))

    elems_missing = elems_needed.difference(elems_of_A)

    if len(elems_missing) == 0:
        return list_elems_of_A[-1] + 1
    else:
        elems_missing = list(elems_missing)
        elems_missing.sort()

        if elems_missing[0] < 1:
            return 1
        else:
            return elems_missing[0]


def solution2(A):
    # write your code in Python 3.6
    """
    55%
    probs:
        +extreme_min_max_value minimal and maximal values
        +positive_only (shuffled sequence of 0...100 and then 102...200)
    """
    len_a = len(A)
    if len_a < 1:
        return 1

    A.sort()
    if A[0] < 1:
        return 1
    else:
        max_val = A[-1]
        present = [-1] * (max_val + 1)

        for i in range(len(A)):
            if A[i] > 0:
                present[A[i]] = 1

        for i, x in enumerate(present[1:]):
            if x != 1:
                return i + 1
        return A[-1] + 1


def solution3(A):
    # write your code in Python 3.6
    """
    100%
    """
    len_a = len(A)
    A.sort()

    if A[0] < 0 and A[-1] < 0:
        return 1
    if len_a == 1 and A[0] != 1:
        return 1

    counter = [0] * (A[-1] + 1)  # should be max_val
    for i in range(len(A)):
        if A[i] > 0:
            counter[A[i]] = 1

    for i, x in enumerate(counter[1:]):
        if x < 1:
            return i + 1

    return A[-1] + 1
