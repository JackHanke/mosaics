
NUM_TILES = 6

def A(k):
    if k == 1: return Matrix(QQ, [[6]])
    else: 
        return block_matrix([
            [NUM_TILES*A(k-1), B(k-1)],
            [C(k-1), D(k-1)]
        ])

def B(k):
    if k == 1: return Matrix(QQ, [[1]])
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

if __name__ == '__main__':
        
    for n in range(2,6):
        m = n
        mn_mosaics_without_polygon = (A(n)**m)[0][0]
        mn_polygons_with_polygons = NUM_TILES**(n*m) - mn_mosaics_without_polygon
        print(f'The number of {m},{n} mosaics that contain atleast one polygon = {mn_polygons_with_polygons}')

