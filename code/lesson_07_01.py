def solution(S):
    # write your code in Python 3.6
    """
    100%
    """

    push_chars = ["(", "{", "["]
    pop_chars = [")", "}", "]"]

    closures = []
    for s in S:
        print("Before: ", closures)
        print(s)
        if s in push_chars:
            closures.append(s)
        if s in pop_chars:
            len_closures = len(closures)
            if len_closures == 0:
                return 0
            head = closures.pop(len_closures - 1)
            print("head: ", head)
            print("s: ", s)
            if head == "(" and s != ")":
                return 0
            if head == "[" and s != "]":
                return 0
            if head == "{" and s != "}":
                return 0
        print("After: ", closures)
    if len(closures) == 0:
        return 1
    else:
        return 0
