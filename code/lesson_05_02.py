def solution(S, P, Q):
    """
    62%
    """
    conversion = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    min_vals = []
    for p, q in zip(P, Q):
        if p == q:
            min_vals.append(conversion[S[p]])
        else:
            substr = list(S[p:q + 1])
            substr.sort()
            min_vals.append(conversion[substr[0]])
    return min_vals


def solution2(S, P, Q):
    """
    100%
    """
    # write your code in Python 3.6
    # A=1
    # C=2
    # T=3
    # G=4
    min_impact = []
    for start, end in zip(P, Q):
        sliced = S[start: end + 1]
        if 'A' in sliced:
            min_impact.append(1)
        elif 'C' in sliced:
            min_impact.append(2)
        elif 'G' in sliced:
            min_impact.append(3)
        else:
            min_impact.append(4)
    return min_impact
