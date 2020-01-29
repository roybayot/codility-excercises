def solution(A):
    # write your code in Python 3.6
    """
    44%

    Does not take into account [-5, -5, 4, 5].
    should give 125 from -5, -5, 5
    """
    A.sort()
    return A[-1]*A[-2]*A[-3]


def solution2(A):
    # write your code in Python 3.6
    """
    100% solution
    """

    prods = []
    A.sort()
    A = A + A[0:2]
    for i in range(0, len(A)-2):
        prods.append(A[i]*A[i+1]*A[i+2])
    prods.sort()

    return prods[-1]
