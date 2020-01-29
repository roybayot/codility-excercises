def solution(A):
    # write your code in Python 3.6
    """
    100% but may need to be changed
    """
    list_set_A = list(set(A))
    return len(list_set_A)


def solution2(A):
    """
    91% did not account for empty
    """
    A.sort()

    B = []
    for i in range(0, len(A) - 1):
        B.append(A[i + 1] - A[i])

    C = [1 for i in B if i != 0]
    return sum(C) + 1
