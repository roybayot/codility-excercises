def solution(n):
    bin_str = bin(n)
    bin_str = bin_str[2:]

    idx_with_ones = [i for i, x in enumerate(bin_str) if x == '1']
    length_idx = len(idx_with_ones)

    num_zeros = []
    for i in range(length_idx):
        if i != length_idx - 1:
            num_zero_for_this_elem = idx_with_ones[i + 1] - idx_with_ones[i] - 1
            num_zeros.append(num_zero_for_this_elem)

    if len(num_zeros) == 0:
        max_num_zero = 0
    else:
        max_num_zero = max(num_zeros)

    print("int: {}, num: {}".format(bin_str, max_num_zero))
    return max_num_zero
    # return binary_gap
