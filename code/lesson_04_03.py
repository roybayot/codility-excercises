"""
MaxCounters
"""


def solution(N, A):
    nums_gt_eq_N = [i for i in A if i >= N]
    nums_lt_N = [i for i in A if i < N]

    num_gt_N = len(nums_gt_eq_N)
    counter = [num_gt_N] * N

    for i in range(1, N + 1):
        count = [1 for ii in nums_lt_N]
        count = sum(count)
        counter[i - 1] = counter[i - 1] + count

    return counter


"""
NOT THE RIGHT ONE
"""
