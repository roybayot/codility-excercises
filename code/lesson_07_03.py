# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution3(A, B):
    """
    37%
    """
    C = [i for i, x in enumerate(B) if x == 1]
    C = [0] + C + [len(A)]

    A_to_compare = None

    fish_downstream = []
    fish_upstream = []
    for i in range(len(C) - 1):
        if i >= 1:
            A_to_compare = A[C[i]]
            fish_stack = A[C[i] + 1:C[i + 1]]

            A_to_compare_not_eaten = True
            while len(fish_stack) > 0 and A_to_compare_not_eaten:
                head = fish_stack.pop(0)
                if A_to_compare > head:
                    continue
                if A_to_compare < head:
                    fish_downstream.append(head)
                    A_to_compare_not_eaten = False

            if len(fish_stack) > 0:
                fish_downstream += fish_stack
            if len(fish_stack) == 0 and A_to_compare_not_eaten:
                fish_upstream.append(A_to_compare)

        else:
            fish_downstream += A[C[i]:C[i + 1]]
    return len(fish_upstream + fish_downstream)


def solution(A, B):

    all_going_right = []
    all_going_left = []
    sample_not_eaten = True
    going_right = []
    for a, b in zip(A, B):
        if b == 0:
            going_right.append(a)
        if b == 1:
            while len(going_right) > 0 and sample_not_eaten:
                tail = going_right.pop(len(going_right) - 1)
                if a >= tail:
                    continue
                else:
                    going_right.append(tail)
                    sample_not_eaten = False

            if sample_not_eaten:
                all_going_left.append(a)

    return len(going_right) + len(all_going_left)


# A = [2,6,4,3,1,5]
# B = [0,1,0,1,0,0]
def solution(A, B):
    """
    100%
    """
    num_survivors = 0
    stack_go_right = []

    for a, b in zip(A, B):
        sample_not_eaten = True
        if b == 0:
            while len(stack_go_right) > 0 and sample_not_eaten:
                tail = stack_go_right.pop(len(stack_go_right) - 1)
                if a >= tail:
                    continue
                else:
                    sample_not_eaten = False
                    stack_go_right.append(tail)
            if sample_not_eaten:
                num_survivors += 1
        if b == 1:
            stack_go_right.append(a)

    return len(stack_go_right) + num_survivors
