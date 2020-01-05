"""
Tape Equilibrium
"""


def solution(A):
    splits = list(range(1, len(A)))
    diff_of_sums = [abs(sum(A[0:i]) - sum(A[i:])) for i in splits]
    return min(diff_of_sums)


def solution2(A):
    left_sum = 0
    right_sum = sum(A)

    abs_diff = []
    for i in range(1, len(A)):
        left_sum = left_sum + A[i - 1]
        right_sum = right_sum - A[i - 1]

        abs_diff.append(abs(left_sum - right_sum))
    return min(abs_diff)
