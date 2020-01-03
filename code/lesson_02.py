def solution(A):
    list_of_unique_elems = list(set(A))
    num_without_pair = None
    for elem in list_of_unique_elems:
        condition = [1 for x in A if x == elem]
        accum = sum(condition)
        if accum % 2 == 1:
            num_without_pair = elem
    return num_without_pair
