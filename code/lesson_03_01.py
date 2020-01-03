"""
Frog jump
"""


def solution(X, Y, D):
    distance = Y - X
    num_jumps = distance // D

    if distance % D != 0:
        num_jumps = num_jumps + 1
    return num_jumps
