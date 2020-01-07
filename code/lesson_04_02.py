"""
FrogRiverOne
"""


def is_equal(items_to_check, A_splice):
    list_A_splice = list(set(A_splice))
    list_A_splice.sort()

    if len(items_to_check) != len(list_A_splice):
        return False
    else:
        diff = [abs(a - b) for a, b in zip(items_to_check, list_A_splice)]
        if sum(diff) == 0:
            return True
        else:
            return False


def solution(X, A):
    items_to_check = list(range(1, X + 1))

    for i in range(X, len(A)):
        A_splice = A[:i]
        if is_equal(items_to_check, A_splice):
            return i - 1

    return -1
    # slice A


def solution2(X, A):
    # write your code in Python 3.6
    """
    correct but not efficient. about 45% correct.
    """
    if len(A) == 0:
        return -1

    count = [0] * (X + 1)
    for i in range(len(A)):
        if A[i] <= X:
            count[A[i]] = count[A[i]] + 1
        if min(count[1:]) != 0:
            return i
    return -1


def solution3(X, A):
    """
    63% correct according to codility
    """
    should_have = list(range(1, X + 1))
    for i in range(len(A)):
        if A[i] in should_have:
            should_have.remove(A[i])
        if len(should_have) == 0:
            return i
    return -1
