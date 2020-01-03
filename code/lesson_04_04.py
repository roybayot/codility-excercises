
def solution(A):
    elems_of_A = set(A)
    list_elems_of_A = list(elems_of_A)
    list_elems_of_A.sort()
    min_elem = list_elems_of_A[0]
    max_elem = list_elems_of_A[-1]

    elems_needed = set(range(min_elem, max_elem + 1))

    elems_missing = elems_needed.difference(elems_of_A)

    if len(elems_missing) == 0:
        return 1
    else:
        elems_missing = list(elems_missing)
        elems_missing.sort()

        if elems_missing[0] < 1:
            return 1
        else:
            return elems_missing[0]
