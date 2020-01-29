# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def prefix_sum(A):
    len_a = len(A)
    pref_sum = [0] * (len_a + 1)

    for i in range(1, len_a + 1):
        pref_sum[i] = pref_sum[i - 1] + A[i - 1]
    return pref_sum


def average_of_slice(pref_sum):
    len_ps = len(pref_sum)

    cumm_sum = pref_sum[-1]

    avgs = []
    for i in range(1, len_ps - 1):
        avg = (cumm_sum - pref_sum[i]) / (len_ps - i)
        avgs.append(avg)
    return avgs


def solution(A):
    # write your code in Python 3.6
    """
    10%
    """
    pref_sum = prefix_sum(A)
    avgs = average_of_slice(pref_sum)
    min_val = avgs[0]
    min_pos = 0
    for i, x in enumerate(avgs):
        if x < min_val:
            min_val = x
            min_pos = i
    return min_pos + 1


# A  =   [4,2,2, 5, 1, 5, 8]
# ps = [0,4,6,8,13,14,19,27]
# av = [3.28, 3.5 , 3.8, 3.5, 4.3, 4.0]

def count_total(P, x, y):
    """
    Accepts a prefix sum, slices
    """
    return P[y + 1] - P[x]


def solution2(A):
    """
    100% solution
    I dont exactly know the insight to this solution
    """

    pref_sum = prefix_sum(A)

    left_idx = 0
    min_left_idx = 0
    min_avg = (A[0] + A[1]) / 2.0
    this_avg = (A[0] + A[1]) / 2.0

    for i in range(2, len(A)):
        prev_avg = count_total(pref_sum, left_idx, i) / (i - left_idx + 1.0)

        avg_of_two = count_total(pref_sum, i - 1, i) / 2.0

        if avg_of_two < prev_avg:
            this_avg = avg_of_two
            left_idx = i - 1
        else:
            this_avg = prev_avg

        if this_avg < min_avg:
            min_avg = this_avg
            min_left_idx = left_idx

    return min_left_idx
