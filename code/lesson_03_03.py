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


def solution3(A):
    if len(A) < 2:
        return 0
    elif len(A) == 2:
        return abs(A[-1] - A[0])
    else:
        left_sum = A[0]
        right_sum = sum(A[1:])
        abs_diff = [abs(right_sum - left_sum)]
        for i in range(1, len(A)):
            left_sum = left_sum + A[i]
            right_sum = right_sum - A[i]
            abs_diff.append(abs(right_sum - left_sum))
        return abs_diff


"""
[-10, -20, -30, -40, 100]
"""
