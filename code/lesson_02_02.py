def solution(A, K):
    rotated = A[-K:] + A[:-K]
    return rotated
