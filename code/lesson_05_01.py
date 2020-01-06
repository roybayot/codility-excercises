def solution(A):
    cars_going_east = [i for i, x in enumerate(A) if x == 0]
    sums_per_split = [sum(A[i:]) for i in cars_going_east]
    total = sum(sums_per_split)
    return total


def solution2(A):
    total_cars_going_west = sums(A)
