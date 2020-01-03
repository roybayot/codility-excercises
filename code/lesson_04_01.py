"""
PermCheck
"""


def count(A, item):
    one_count = [1 for a in A if a == item]
    return sum(one_count)


def solution(A):
    is_permutation = False
    items = list(range(1, len(A) + 1))

    counts_per_item = [count(A, item) for item in items]
    list_unique_counts = list(set(counts_per_item))

    if len(list_unique_counts) == 1 and list_unique_counts[0] == 1:
        return 1  # it is a permutation
    else:
        return 0
