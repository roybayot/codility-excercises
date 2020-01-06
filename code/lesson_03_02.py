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


def bin_search(A):
    len_A = len(A)

    if len(A) == 2:
        return A[0] + 1
    else:
        mid_idx = len_A // 2
        left = A[:mid_idx]
        right = A[mid_idx:]

        len_left = len(left)
        len_right = len(right)

        if (left[0] + len(left) - 1 != left[-1]):
            return bin_search(left)
        else:
            return bin_search(right)


def solution2(A):
    # write your code in Python 3.6
    A.sort()
    return search2(A)


def search2(A):
    print("Input array:")
    print(A)
    len_A = len(A)
    start_A = A[0]
    end_A = A[-1]

    if len_A == 2 and end_A - start_A != 1:
        return start_A + 1

    else:
        mid_idx = len_A // 2
        left = A[:mid_idx]
        right = A[mid_idx:]

        print("left")
        print(left)
        print("right")
        print(right)

        if right[0] - left[-1] != 1:
            return left[-1] + 1

        if (left[0] + len(left) - 1 != left[-1]):
            return search2(left)
        else:
            return search2(right)


"""
def binary_search(A):
    A.sort()
    first = A[0]
    last = A[-1]
    found = False
    while (first <= last and not found):
        mid_idx = len(A) // 2
        if A[mid_idx] - A[0] != 1:
            found = True
            return A[0]+1
        else:
            if
"""
