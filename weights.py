# NOTE this code is so ugly

special_cases = [
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
]

def base_to_list(value, length, base):
    num_digits = length
    rep = []
    for _ in range(length):
        rep.append(value % base)
        value = value // base
    return rep

def identify_weights(vertices):
    v1,v2,v3,v4,v6,v7,v8,v9 = vertices
    # map vertex parity to weight index
    weight_map = {
        (0,0,0,0):0,
        (0,0,0,1):1,
        (0,0,1,0):2,
        (0,0,1,1):3,
        (0,1,0,0):4,
        (0,1,0,1):5,
        (0,1,1,0):6,
        (0,1,1,1):7,
        (1,0,0,0):8,
        (1,0,0,1):9,
        (1,0,1,0):10,
        (1,0,1,1):11,
        (1,1,0,0):12,
        (1,1,0,1):13,
        (1,1,1,0):14,
        (1,1,1,1):15
    }
    # weights involved in the constraint
    weights_left = [weight_map[(v1,v2,v4,0)], weight_map[(v2,v3,0,v6)], weight_map[(v4,0,v7,v8)], weight_map[(0,v6,v8,v9)]]
    weights_right = [weight_map[(v1,v2,v4,1)], weight_map[(v2,v3,1,v6)], weight_map[(v4,1,v7,v8)], weight_map[(1,v6,v8,v9)]]
    return weights_left, weights_right

def test_weights(weights, verbose=False):
    constraints_str = ''
    col = 0

    i = 0
    for val in range(2**8):
        v1, v2, v3, v4, v6, v7, v8, v9 = base_to_list(value=val, length=8, base=2)
        vertices = [v1,v2,v3,v4,v6,v7,v8,v9]
        # if vertices aren't the two special cases
        if vertices not in [[0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1]]:
            weights_left, weights_right = identify_weights(vertices=vertices)
            # avoid checking constraints that involve the non-existent tiles for w_7 and w_10
                # pass
            
            # NOTE there are certain special cases in which the change in a cell SHOULD flip the weight product
            # these are the situations where EITHER two seperate regions of the same SAP combine to make two unique SAPs
            #   OR two seperate SAPs combine to make one SAP. Either way the product should flip sign

            
            # 
            prod_left = 1
            for index in weights_left: prod_left *= weights[index]
            prod_right = 1
            for index in weights_right: prod_right *= weights[index]
            

            if vertices in special_cases: 
                prod_left *= -1
            if prod_left != prod_right: return False

            # format constraints string
            constraint_str = ''
            if vertices not in special_cases: 
                # constraint_str += '-'
                for index in weights_left: constraint_str += 'w_{' + str(index+1) + '}'
                constraint_str += ' = '
                for index in weights_right: constraint_str += 'w_{' + str(index+1) + '}'
                if col == 0 or col == 1:
                    constraint_str += ' & '
                if col == 2:
                    constraint_str += ' \\\\\n'
                col = ((col+1)%3)
                constraints_str += constraint_str 

    if verbose: print(constraints_str)
    return True

def get_solutions(verbose=False):
    solution_set = []
    # loop over all possible weight signs
    for val in range(2**16):
        weights = base_to_list(value=val, length=16, base=2)
        weights_signs = [2*w - 1 for w in weights]
        w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9, w_10, w_11, w_12, w_13, w_14, w_15, w_16 = weights_signs
        # initial check that smallest two knots can be created
        if w_2*w_3*w_5*w_9 == -1 and w_15*w_14*w_12*w_8 == -1:
            # more in-depth check
            if test_weights(weights=weights_signs, verbose=verbose): 
                solution_set.append(weights_signs)
    return solution_set

def make_A_from_weights(weights: dict):
    A = matrix(QQ, 
        [
            [weights[1]*weights[1],weights[2]*weights[5]],
            [weights[3]*weights[9],weights[4]*weights[13]],
        ]
    )

    return A

def make_V_from_weights(weights: dict):
    V = matrix(QQ, 
        [
            [weights[1],weights[2]*weights[5]/weights[1],weights[1],weights[6]],
            [weights[3]*weights[9]/weights[1],weights[4]*weights[13]/weights[1],weights[3]*weights[10]/weights[2],weights[4]*weights[14]/weights[2]],
            [weights[1],weights[2]*weights[7]/weights[3],weights[1],weights[2]*weights[8]/weights[4]],
            [weights[11],weights[4]*weights[15]/weights[3],weights[3]*weights[12]/weights[4],weights[16]],
        ]
    )

    return V

if __name__ == '__main__':
    # NOTE check weights discovered solve all constraints
    # weights = [1,1,1,1,1,1,0,1,-1,0,1,1,1,1,-1,1]
    # print(test_weights(weights=weights, verbose=True))
    # for val in range(2**8):
    #     v1, v2, v3, v4, v6, v7, v8, v9 = base_to_list(value=val, length=8, base=2)
    #     vertices = [v1,v2,v3,v4,v6,v7,v8,v9]
    #     print(vertices)

    # weights = [1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1]
    # print(test_weights(weights=weights, verbose=False))


    # # NOTE generates total solution set
    solution_set = get_solutions()

    unique_As = []
    unique_Vs = []

    for sol_num, sol in enumerate(solution_set):
        sol_string = f'{sol_num+1} :: {sol}'
        # for num in sol:
        #     thing += str(num) + ' & '
        # thing += ' \\\\'
        # print(sol_string)

        # print(f'[w_1 ... w_16] & = & {[6] +sol[1:-1] + [6]} \\\\')

        A = make_A_from_weights(weights=sol)
        if A not in unique_As: unique_As.append(A)
        V = make_V_from_weights(weights=sol)
        if V not in unique_Vs: unique_As.append(V)
    
    


    '''
    Notes from debug:
    Check out the following:
    38,39,40,41,52,53,54,55,75,102,103,104,105,116,117,118
    '''

    '''
    No flip:
    [1, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 1, 0, 0, 0, 0, 0]
    [0, 1, 0, 1, 0, 0, 0, 0]
    [0, 1, 1, 1, 0, 0, 0, 0]
    [0, 1, 0, 0, 1, 0, 0, 0]



    '''
    '''
    Flip:
    [1, 0, 1, 0, 0, 0, 0, 0]
    [0, 0, 1, 1, 0, 0, 0, 0]
    [1, 0, 1, 1, 0, 0, 0, 0]
    [1, 0, 0, 0, 1, 0, 0, 0]

    [1, 1, 0, 0, 1, 0, 0, 0]
    [1, 0, 1, 0, 1, 0, 0, 0]
    [0, 1, 0, 1, 1, 0, 0, 0]
    [1, 1, 0, 1, 1, 0, 0, 0]
    [0, 1, 1, 1, 1, 0, 0, 0]
    [0, 0, 0, 0, 0, 1, 0, 0]
    [1, 0, 0, 0, 0, 1, 0, 0]
    [0, 1, 0, 0, 0, 1, 0, 0]
    [1, 1, 0, 0, 0, 1, 0, 0]
    [0, 0, 1, 0, 0, 1, 0, 0]
    [1, 0, 1, 0, 0, 1, 0, 0]
    [0, 1, 1, 0, 0, 1, 0, 0]
    [1, 1, 1, 0, 0, 1, 0, 0]
    [0, 1, 0, 1, 0, 1, 0, 0]
    [0, 0, 1, 1, 0, 1, 0, 0]
    [1, 0, 1, 1, 0, 1, 0, 0]
    [0, 1, 1, 1, 0, 1, 0, 0]
    [0, 0, 0, 0, 1, 1, 0, 0]
    [1, 0, 0, 0, 1, 1, 0, 0]
    [0, 1, 0, 0, 1, 1, 0, 0]
    [1, 1, 0, 0, 1, 1, 0, 0]
    [0, 0, 1, 0, 1, 1, 0, 0]
    [1, 0, 1, 0, 1, 1, 0, 0]
    [0, 1, 1, 0, 1, 1, 0, 0]
    [1, 1, 1, 0, 1, 1, 0, 0]
    [0, 1, 0, 1, 1, 1, 0, 0]
    [1, 1, 0, 1, 1, 1, 0, 0]
    [0, 1, 1, 1, 1, 1, 0, 0]
    [1, 0, 0, 0, 0, 0, 1, 0]
    [0, 0, 1, 0, 0, 0, 1, 0]
    [1, 0, 1, 0, 0, 0, 1, 0]
    [0, 0, 0, 1, 0, 0, 1, 0]
    [1, 0, 0, 1, 0, 0, 1, 0]
    [0, 1, 0, 1, 0, 0, 1, 0]
    [1, 1, 0, 1, 0, 0, 1, 0]
    [0, 0, 1, 1, 0, 0, 1, 0]
    [1, 0, 1, 1, 0, 0, 1, 0]
    [0, 1, 1, 1, 0, 0, 1, 0]
    [1, 1, 1, 1, 0, 0, 1, 0]
    [0, 0, 0, 0, 1, 0, 1, 0]
    [1, 0, 0, 0, 1, 0, 1, 0]
    [0, 1, 0, 0, 1, 0, 1, 0]
    [1, 1, 0, 0, 1, 0, 1, 0]
    [0, 0, 1, 0, 1, 0, 1, 0]
    [1, 0, 1, 0, 1, 0, 1, 0]
    [0, 1, 1, 0, 1, 0, 1, 0]
    [1, 1, 1, 0, 1, 0, 1, 0]
    [0, 0, 0, 1, 1, 0, 1, 0]
    [1, 0, 0, 1, 1, 0, 1, 0]
    [0, 1, 0, 1, 1, 0, 1, 0]
    [1, 1, 0, 1, 1, 0, 1, 0]
    [0, 0, 1, 1, 1, 0, 1, 0]
    [1, 0, 1, 1, 1, 0, 1, 0]
    [0, 1, 1, 1, 1, 0, 1, 0]
    [1, 1, 1, 1, 1, 0, 1, 0]
    [1, 0, 0, 0, 0, 1, 1, 0]
    [0, 0, 1, 0, 0, 1, 1, 0]
    [1, 0, 1, 0, 0, 1, 1, 0]
    [0, 1, 0, 1, 0, 1, 1, 0]
    [0, 0, 1, 1, 0, 1, 1, 0]
    [1, 0, 1, 1, 0, 1, 1, 0]
    [0, 1, 1, 1, 0, 1, 1, 0]
    [0, 0, 0, 0, 1, 1, 1, 0]
    [1, 0, 0, 0, 1, 1, 1, 0]
    [0, 1, 0, 0, 1, 1, 1, 0]
    [1, 1, 0, 0, 1, 1, 1, 0]
    [0, 0, 1, 0, 1, 1, 1, 0]
    [1, 0, 1, 0, 1, 1, 1, 0]
    [0, 1, 1, 0, 1, 1, 1, 0]
    [1, 1, 1, 0, 1, 1, 1, 0]
    [0, 0, 0, 1, 1, 1, 1, 0]
    [1, 0, 0, 1, 1, 1, 1, 0]
    [0, 1, 0, 1, 1, 1, 1, 0]
    [1, 1, 0, 1, 1, 1, 1, 0]
    [0, 0, 1, 1, 1, 1, 1, 0]
    [1, 0, 1, 1, 1, 1, 1, 0]
    [0, 1, 1, 1, 1, 1, 1, 0]
    [1, 1, 1, 1, 1, 1, 1, 0]
    [0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 1]
    [0, 1, 0, 0, 0, 0, 0, 1]
    [1, 1, 0, 0, 0, 0, 0, 1]
    [0, 0, 1, 0, 0, 0, 0, 1]
    [1, 0, 1, 0, 0, 0, 0, 1]
    [0, 1, 1, 0, 0, 0, 0, 1]
    [1, 1, 1, 0, 0, 0, 0, 1]
    [0, 0, 0, 1, 0, 0, 0, 1]
    [1, 0, 0, 1, 0, 0, 0, 1]
    [0, 1, 0, 1, 0, 0, 0, 1]
    [1, 1, 0, 1, 0, 0, 0, 1]
    [0, 0, 1, 1, 0, 0, 0, 1]
    [1, 0, 1, 1, 0, 0, 0, 1]
    [0, 1, 1, 1, 0, 0, 0, 1]
    [1, 1, 1, 1, 0, 0, 0, 1]
    [1, 0, 0, 0, 1, 0, 0, 1]
    [0, 1, 0, 0, 1, 0, 0, 1]
    [1, 1, 0, 0, 1, 0, 0, 1]
    [1, 0, 1, 0, 1, 0, 0, 1]
    [0, 1, 0, 1, 1, 0, 0, 1]
    [1, 1, 0, 1, 1, 0, 0, 1]
    [0, 1, 1, 1, 1, 0, 0, 1]
    [0, 0, 0, 0, 0, 1, 0, 1]
    [1, 0, 0, 0, 0, 1, 0, 1]
    [0, 1, 0, 0, 0, 1, 0, 1]
    [1, 1, 0, 0, 0, 1, 0, 1]
    [0, 0, 1, 0, 0, 1, 0, 1]
    [1, 0, 1, 0, 0, 1, 0, 1]
    [0, 1, 1, 0, 0, 1, 0, 1]
    [1, 1, 1, 0, 0, 1, 0, 1]
    [0, 0, 0, 1, 0, 1, 0, 1]
    [1, 0, 0, 1, 0, 1, 0, 1]
    [0, 1, 0, 1, 0, 1, 0, 1]
    [1, 1, 0, 1, 0, 1, 0, 1]
    [0, 0, 1, 1, 0, 1, 0, 1]
    [1, 0, 1, 1, 0, 1, 0, 1]
    [0, 1, 1, 1, 0, 1, 0, 1]
    [1, 1, 1, 1, 0, 1, 0, 1]
    [0, 0, 0, 0, 1, 1, 0, 1]
    [1, 0, 0, 0, 1, 1, 0, 1]
    [0, 1, 0, 0, 1, 1, 0, 1]
    [1, 1, 0, 0, 1, 1, 0, 1]
    [0, 0, 1, 0, 1, 1, 0, 1]
    [1, 0, 1, 0, 1, 1, 0, 1]
    [0, 1, 1, 0, 1, 1, 0, 1]
    [1, 1, 1, 0, 1, 1, 0, 1]
    [0, 1, 0, 1, 1, 1, 0, 1]
    [1, 1, 0, 1, 1, 1, 0, 1]
    [0, 1, 1, 1, 1, 1, 0, 1]
    [1, 0, 0, 0, 0, 0, 1, 1]
    [0, 0, 1, 0, 0, 0, 1, 1]
    [1, 0, 1, 0, 0, 0, 1, 1]
    [0, 0, 0, 1, 0, 0, 1, 1]
    [1, 0, 0, 1, 0, 0, 1, 1]
    [0, 1, 0, 1, 0, 0, 1, 1]
    [1, 1, 0, 1, 0, 0, 1, 1]
    [0, 0, 1, 1, 0, 0, 1, 1]
    [1, 0, 1, 1, 0, 0, 1, 1]
    [0, 1, 1, 1, 0, 0, 1, 1]
    [1, 1, 1, 1, 0, 0, 1, 1]
    [1, 0, 0, 0, 1, 0, 1, 1]
    [0, 1, 0, 0, 1, 0, 1, 1]
    [1, 1, 0, 0, 1, 0, 1, 1]
    [1, 0, 1, 0, 1, 0, 1, 1]
    [0, 0, 0, 1, 1, 0, 1, 1]
    [1, 0, 0, 1, 1, 0, 1, 1]
    [0, 1, 0, 1, 1, 0, 1, 1]
    [1, 1, 0, 1, 1, 0, 1, 1]
    [0, 0, 1, 1, 1, 0, 1, 1]
    [1, 0, 1, 1, 1, 0, 1, 1]
    [0, 1, 1, 1, 1, 0, 1, 1]
    [1, 1, 1, 1, 1, 0, 1, 1]
    [1, 0, 0, 0, 0, 1, 1, 1]
    [0, 0, 1, 0, 0, 1, 1, 1]
    [1, 0, 1, 0, 0, 1, 1, 1]
    [0, 1, 0, 1, 0, 1, 1, 1]
    [0, 0, 1, 1, 0, 1, 1, 1]
    [1, 0, 1, 1, 0, 1, 1, 1]
    [0, 1, 1, 1, 0, 1, 1, 1]
    [1, 0, 0, 0, 1, 1, 1, 1]
    [0, 1, 0, 0, 1, 1, 1, 1]
    [1, 1, 0, 0, 1, 1, 1, 1]
    [1, 0, 1, 0, 1, 1, 1, 1]
    [0, 1, 0, 1, 1, 1, 1, 1]
    [1, 1, 0, 1, 1, 1, 1, 1]
    [0, 1, 1, 1, 1, 1, 1, 1]
    '''
