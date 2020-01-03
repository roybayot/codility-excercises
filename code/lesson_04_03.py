"""
MaxCounters
"""


def solution(N, A):
    bins = [0] * N
    max_count = 0

    for i in A:
        if i == N + 1:
            bins = [max_count] * N
        if 1 <= i and i <= N:
            bins[i - 1] = bins[i - 1] + 1
        max_count = max(bins)

    return bins

