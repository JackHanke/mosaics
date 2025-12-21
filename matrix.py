from time import time
import numpy as np
import torch

NUM_TILES = 6

# real matrixes

def A(k):
    if k == 1: return torch.tensor([[6]], dtype=torch.long, requires_grad=False)
    else: 
        temp1 = torch.cat([NUM_TILES*pA(k-1), pB(k-1)], axis=1)
        temp2 = torch.cat([pC(k-1), pD(k-1)], axis=1)
        return torch.cat([temp1, temp2], axis=0)

def B(k):
    if k == 1: return torch.tensor([[-1]], dtype=torch.long, requires_grad=False)
    else: 
        temp1 = torch.cat([-1*pA(k-1), pB(k-1)], axis=1)
        temp2 = torch.cat([0*pC(k-1), pD(k-1)], axis=1)
        return torch.cat([temp1, temp2], axis=0)

def C(k):
    if k == 1: return torch.tensor([[1]], dtype=torch.long, requires_grad=False)
    else: 
        temp1 = torch.cat([pA(k-1), 0*pB(k-1)], axis=1)
        temp2 = torch.cat([pC(k-1), pD(k-1)], axis=1)
        return torch.cat([temp1, temp2], axis=0)

def D(k):
    if k == 1: return torch.tensor([[1]], dtype=torch.long, requires_grad=False)
    else: 
        temp1 = torch.cat([pA(k-1), -1*pB(k-1)], axis=1)
        temp2 = torch.cat([pC(k-1), NUM_TILES*pD(k-1)], axis=1)
        return torch.cat([temp1, temp2], axis=0)

## probability matrixes

def pA(k):
    if k == 1: return torch.tensor([[6]], dtype=torch.long, requires_grad=False)/NUM_TILES
    else: 
        temp1 = torch.cat([NUM_TILES*pA(k-1), pB(k-1)], axis=1)
        temp2 = torch.cat([pC(k-1), pD(k-1)], axis=1)
        return torch.cat([temp1, temp2], axis=0)/NUM_TILES

def pB(k):
    if k == 1: return torch.tensor([[-1]], dtype=torch.long, requires_grad=False)/NUM_TILES
    else: 
        temp1 = torch.cat([-1*pA(k-1), pB(k-1)], axis=1)
        temp2 = torch.cat([0*pC(k-1), pD(k-1)], axis=1)
        return torch.cat([temp1, temp2], axis=0)/NUM_TILES

def pC(k):
    if k == 1: return torch.tensor([[1]], dtype=torch.long, requires_grad=False)/NUM_TILES
    else: 
        temp1 = torch.cat([pA(k-1), 0*pB(k-1)], axis=1)
        temp2 = torch.cat([pC(k-1), pD(k-1)], axis=1)
        return torch.cat([temp1, temp2], axis=0)/NUM_TILES

def pD(k):
    if k == 1: return torch.tensor([[1]], dtype=torch.long, requires_grad=False)/NUM_TILES
    else: 
        temp1 = torch.cat([pA(k-1), -1*pB(k-1)], axis=1)
        temp2 = torch.cat([pC(k-1), NUM_TILES*pD(k-1)], axis=1)
        return torch.cat([temp1, temp2], axis=0)/NUM_TILES

if __name__ == '__main__':
    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # for n in range(2,6):
    #     m = n
    #     mn_mosaics_without_polygon = (A(n)**m)[0][0]
    #     mn_polygons_with_polygons = NUM_TILES**(n*m) - mn_mosaics_without_polygon
    #     print(f'The number of {m},{n} mosaics that contain atleast one polygon = {mn_polygons_with_polygons}')

    # for n in range(2, 7):
    #     start = time()
    #     m = 2
    #     mat_A = pA(n)
    #     partial_A = torch.matmul(mat_A, mat_A)
    #     prob = 1 - partial_A[0][0]
    #     while prob < 0.5:
    #         m += 1
    #         partial_A = torch.matmul(partial_A, mat_A)
    #         prob = 1 - partial_A[0][0]
    #     print(f'{m} (in {time()-start:.2f}s) is the smallest m such that an {n},m mosaic has greater than 50% change of containing at least one polygon.')

    size = 7
    arr = np.zeros((size, size))
    for n in range(2, size):
        mat_A = pA(n)
        partial_A = torch.matmul(mat_A, mat_A)
        for m in range(2, n):
            
            arr[n][m] = 6**(n*m) - partial_A[0][0]
            partial_A = torch.matmul(partial_A, mat_A)

    print(arr)

