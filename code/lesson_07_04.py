def solution(H):
    one_cube = H[0]
    prev_cube = H[0]

    first_stack = []
    first_stack.append(prev_cube)

    main_stack = []
    sub_stack = []

    for h in H:
        if h < prev_cube:
            first_stack.append(h)
            prev_cube = h
            main_stack.append(sub_stack)
        else:
            sub_stack.append(h)

    for stack in sub_stack:


def solution(H):

    stack = []
    prev_cube = H[0]
    accepted_block = []
    accepted_block.append(prev_cube)
    for h in H:
        if h <= prev_cube:
            accepted_block.append(h)
            prev_cube = h
        else:
            stack.append(h)
