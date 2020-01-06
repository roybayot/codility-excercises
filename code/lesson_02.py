def solution(A):
    list_of_unique_elems = list(set(A))
    num_without_pair = None
    for elem in list_of_unique_elems:
        condition = [1 for x in A if x == elem]
        accum = sum(condition)
        if accum % 2 == 1:
            num_without_pair = elem
    return num_without_pair


def solution2(A):
    unpaired = [A[0]]

    for each_elem in A[1:]:
        matched = False
        num_unpaired = len(unpaired)
        i = 0
        while i < num_unpaired and not matched:
            if each_elem == unpaired[i]:
                unpaired.pop(i)
                matched = True
            else:
                i = i + 1
        if not matched:
            unpaired.append(each_elem)

    return unpaired[0]


def solution3(A):
    A.sort()
    A = A + [A[-1]]
    for x in range(0, len(A), 2):
        a = A[x]
        b = A[x + 1]
        if a != b:
            return a
    return A[-1]
