"""
MaxCounters
"""


def solution(N, A):
    """
    66%
    not okay for large random test, 2120 max_counter
    not okay large random test, 10000 max_counter
    not okay all max_counter operations
    """
    bins = [0] * N
    max_count = 0

    for i in A:
        if i == N + 1:
            bins = [max_count] * N
        if 1 <= i and i <= N:
            bins[i - 1] = bins[i - 1] + 1
        max_count = max(bins)

    return bins



def solution2(N, A):
    # write your code in Python 3.6
    """
    88%
    does not work on extremely large numbers
    """

    counter = [0]*N

    max_counter = 0

    for i in range(len(A)):
        if 1 <= A[i] <= N:
            counter[A[i]-1] += 1

            if counter[A[i]-1] > max_counter:
                max_counter = counter[A[i]-1]
        else:
            counter = [max_counter]*N

    return counter
