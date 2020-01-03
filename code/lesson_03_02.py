"""
perm missing elem
"""


def solution(A):
    set_of_nums_to_have = set(list(range(1, len(A) + 1)))
    set_A = set(A)

    missing_num = list(set_of_nums_to_have - set_of_nums_to_have.intersection(set_A))
    if len(missing_num) == 1:
        return missing_num[0]
    else:
        return 0
