# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    """
    100%
    """
    push_chars = ["("]
    pop_chars = [")"]

    if len(S) == 0: # why is empty string considered proper nesting?
        return 1

    closures = []

    for s in S:
        if s in push_chars:
            closures.append(s)
        if s in pop_chars:
            if len(closures) == 0:
                return 0
            tail = closures.pop(len(closures)-1)
            if tail == "(" and s != ")":
                return 0
    if len(closures) == 0:
        return 1
    else:
        return 0
