from numpy import zeros
from copy import deepcopy
from time import time

def saps_help(allsaps,plane,walk,h,w,curri,currj,pasti,pastj,starti,startj):
    walk = deepcopy(walk)
    if curri == starti and currj == startj: 
        allsaps.append(tuple(walk))

    if ((curri < h) and (curri>=0) and (currj < w) and ((curri >= starti and currj >= startj) or (curri < starti and currj > startj))):
        if ((curri,currj) not in walk) and plane[curri][currj] == 0:
            walk.append((curri,currj))
            # right
            saps_help(allsaps, plane, walk, h, w, (curri + currj - pastj), (currj + pasti - curri), curri, currj, starti, startj)
            # forward
            saps_help(allsaps, plane, walk, h, w, ((2*curri) - pasti), ((2*currj)-pastj), curri, currj, starti, startj)
            # left
            saps_help(allsaps, plane, walk, h, w, (curri + pastj - currj), (currj + curri - pasti), curri, currj, starti, startj)

def saps(plane,starti,startj,h,w):
    allsaps = []
    walk = [(starti,startj)]
    saps_help(allsaps, plane, walk, h, w, starti+1, startj, starti, startj, starti, startj)
    return allsaps

def memoize_check(saps_set, memoize): return saps_set in memoize
    
def mosaics_help(plane, memoize, saps_list, opens, depth, h, w):
    return_val = 0
    for i in range(h-1):
        for j in range(w-1):
            if plane[i][j] == 0: 
                workingsaps = saps(plane,i,j,h,w)
                if len(workingsaps) == 0: plane[i][j] = 1
                else:
                    for sap in workingsaps:
                        copy_plane = deepcopy(plane)
                        for sap_elem in sap: copy_plane[sap_elem[0]][sap_elem[1]] = 1
                        
                        copy_saps_list = deepcopy(saps_list)
                        already_seen = memoize_check(set(tuple(copy_saps_list+[sap])),memoize)

                        if not already_seen:
                            copy_saps_list.append(sap)
                            memoize.append(set(tuple(copy_saps_list)))
                            to_add = ((6**(opens - len(sap))) * ((-1)**(depth % 2)))
                            return_val += to_add + mosaics_help(copy_plane, memoize, copy_saps_list, opens-len(sap), depth+1, h, w )                        
    return return_val

def mosaics(h,w):
    plane = zeros((h,w))
    saps_list, memoize = [], []
    return mosaics_help(plane, memoize, saps_list, h*w, 0, h, w)

if __name__ == '__main__':
    for n in range(2,5):
        for m in range(n,5):
            value = mosaics(n,m)
            print(f't_{n,m} = {value}')
