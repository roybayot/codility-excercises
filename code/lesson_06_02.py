def solution(A):
    # write your code in Python 3.6
    """
    100%
    Dont know why P,Q,R does not matter.
    """
    if len(A) < 3:
        return 0

    A.sort()

    for i in range(0, len(A)-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0
