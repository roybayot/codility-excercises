"""
Tape Equilibrium
"""


def solution(A):
    splits = list(range(1, len(A)))
    diff_of_sums = [abs(sum(A[0:i]) - sum(A[i:])) for i in splits]
    return min(diff_of_sums)
