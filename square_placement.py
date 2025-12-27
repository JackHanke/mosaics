## functions for computing how many ways one can place k non-overlapping 2 x 2 squares in an m x n rectangular grid



n = 4
m = 4

# A061995 on OEIS
def two_squares_in_grid_no_overlap(m:int, n: int):
    tot = 0
    for i_1 in range(m-1):
        for j_1 in range(n-1):
            # print(f'Square 1: ({i_1},{j_1})')
            for i_2 in range(i_1+1):
                thing = j_1 if i_2 == i_1 else n-1
                for j_2 in range(thing):
                    # print(f'Considering ({i_1},{j_1}) ({i_2},{j_2})')
                    if i_1 - i_2 > 1 or abs(j_1 - j_2) > 1:
                        # print(f'Found ({i_1},{j_1}) ({i_2},{j_2})')
                        tot += 1
    return tot

# tot = two_squares_in_grid_no_overlap(m=4, n=3)
# tot = two_squares_in_grid_no_overlap(m=4, n=4)
# print(tot)

for n in range(2, 15):
    val = two_squares_in_grid_no_overlap(m=n-1, n=n)
    print(f'{val}, ', end='')




#        (n-1)^2 6^{n^2 - 4} - (n-1)^4 6^{n^2 - 8} > 3*6^{n^2-1}
#        (n-1)^2 6^4 - (n-1)^4 > 3*6^7

#        6^4 x - x^2 > 3*6^7
#        0 > x^2 - 6^4x + 3*6^7



