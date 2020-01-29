from operator import itemgetter


def solution(A):
    # write your code in Python 3.6
    """
    12% WTF
    """
    start_end = []
    for i, x in enumerate(A):
        start_end.append([i - x, 1])  # start
        start_end.append([i + x, -1]  # end
    sorted_start_end=sorted(start_end, key=itemgetter(0))
    stacked_under=0
    intersections=0
    for a in sorted_start_end:
        if a[1] == 1:
            stacked_under=stacked_under + 1
            intersections=intersections + stacked_under - 1
        if a[1] == -1:
            stacked_under=stacked_under - 1
    if intersections > 10000000:
        return 0
    return intersections
