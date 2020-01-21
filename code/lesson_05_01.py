def solution(A):
    cars_going_east = [i for i, x in enumerate(A) if x == 0]
    sums_per_split = [sum(A[i:]) for i in cars_going_east]
    total = sum(sums_per_split)
    return total


def prefix_sum(A):
    len_a = len(A)
    pref_sum = [0] * (len_a + 1)

    for i in range(1, len_a + 1):
        pref_sum[i] = pref_sum[i - 1] + A[i - 1]

    return pref_sum


def suffix_sum(A):
    len_a = len(A)
    suf_sum = [0] * (len_a + 1)
    for i in range(len(A) - 1, -1, -1):
        suf_sum[i] = A[i] + suf_sum[i + 1]
    return suf_sum


def solution2(A):
    # write your code in Python 3.6
    pref_sum_A = prefix_sum(A)
    total = pref_sum_A[-1]

    accum = 0
    for i in range(len(A)):
        if A[i] == 0:
            accum = accum + total - pref_sum_A[i + 1]
        if accum > 1000000: # condition i did not check
            return -1
    return accum
