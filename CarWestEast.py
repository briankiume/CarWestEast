
def len_pairs(a):
    a_in = []
    for i, num in enumerate(a):
        a_in.append((num, i))

    a_0 = []
    a_1 = []
    for x in a_in:
        if x[0] == 0:
            a_0.append(x)
        if x[0] == 1:
            a_1.append(x)

    pairs = []
    for num_x, ind_x in a_0:
        for num_y, ind_y in a_1:
            if ind_x < ind_y:
                pairs.append((ind_x, ind_y))

    if len(pairs) > 1000000:
        number_of_pairs = -1
    else:
        number_of_pairs = len(pairs)

    return number_of_pairs


print(len_pairs([0, 1, 0, 1, 1]))
