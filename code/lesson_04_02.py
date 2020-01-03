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
