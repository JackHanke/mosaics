from sage.all import *

NUM_TILES = 6

def A(k):
    if k == 1: return Matrix(QQ, [[6]])
    else: 
        return block_matrix([
            [NUM_TILES*A(k-1), B(k-1)],
            [C(k-1), D(k-1)]
        ])

def B(k):
    if k == 1: return Matrix(QQ, [[-1]])
    else: 
        return block_matrix([
            [-1*A(k-1), B(k-1)],
            [0*C(k-1), D(k-1)]
        ])

def C(k):
    if k == 1: return Matrix(QQ, [[1]])
    else: 
        return block_matrix([
            [A(k-1), 0*B(k-1)],
            [C(k-1), D(k-1)]
        ])

def D(k):
    if k == 1: return Matrix(QQ, [[1]])
    else: 
        return block_matrix([
            [A(k-1), -1*B(k-1)],
            [C(k-1), NUM_TILES*D(k-1)]
        ])

# if __name__ == '__name__':
# size = 8
# # arr = 
# for n in range(2, size):
#     mat_A = A(n)
#     partial_A = mat_A * mat_A
#     for m in range(2, n+1):
#         value = 6**(n*m) - partial_A[0][0]
#         # arr[m][n] = value
#         print(f'arr[{m}][{n}] = {value}')
#         if m != n:
#             partial_A *= mat_A

## growth rate
size = 11
# lst = [(A(n)**n)[0][0] for n in range(2, size)]
lst = [sum(sum(A(n)**n)) for n in range(2, size)]

# a^(n+1)^2 / a^n^2 = a^(2*n+1)
for i in range(len(lst)-1):
    print(((lst[i+1]/lst[i])**(1/(1+2*(i+2)))))
