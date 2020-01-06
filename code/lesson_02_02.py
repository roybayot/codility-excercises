def solution(A, K):
    rotated = A[-K:] + A[:-K]
    return rotated


def solution2(A, K):
    len_A = len(A)
    rotated = [0] * len_A
    for i in range(len_A):
        rotated[(i + K) % len_A] = A[i]

    return rotated
