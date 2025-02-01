# NOTE this code is so ugly

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
    for v1 in [0,1]:
        for v2 in [0,1]:
            for v3 in [0,1]:
                for v4 in [0,1]:
                    for v6 in [0,1]:
                        for v7 in [0,1]:
                            for v8 in [0,1]:
                                for v9 in [0,1]:
                                    vertices = [v1,v2,v3,v4,v6,v7,v8,v9]
                                    # if vertices aren't the two special cases
                                    if vertices not in [[0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1]]:
                                        weights_left, weights_right = identify_weights(vertices=vertices)
                                        # avoid checking constraints that involve the non-existent tiles for w_7 and w_10
                                        if 6 not in weights_left and 6 not in weights_right and 9 not in weights_left and 9 not in weights_right:
                                            constraint_str = ''
                                            # 
                                            prod_left = 1
                                            for index in weights_left: prod_left *= weights[index]
                                            prod_right = 1
                                            for index in weights_right: prod_right *= weights[index]

                                            # NOTE there are certain special cases in which the change in a cell SHOULD flip the weight product
                                            # these are the situations where EITHER two seperate regions of the same SAP combine to make two unique SAPs
                                            #   OR two seperate SAPs combine to make one SAP. Either way 
                                            special_cases = [
                                                [0, 0, 0, 1, 1, 0, 0, 0],
                                                [0, 0, 0, 1, 1, 0, 0, 1],
                                                [0, 0, 0, 1, 1, 1, 0, 0],
                                                [0, 0, 0, 1, 1, 1, 0, 1],
                                                [0, 0, 1, 1, 1, 0, 0, 0],
                                                [0, 0, 1, 1, 1, 0, 0, 1],
                                                [0, 0, 1, 1, 1, 1, 0, 0],
                                                [0, 0, 1, 1, 1, 1, 0, 1],
                                                [0, 1, 0, 0, 0, 0, 1, 0],
                                                [0, 1, 0, 0, 0, 0, 1, 1],
                                                [0, 1, 0, 0, 0, 1, 1, 0],
                                                [0, 1, 0, 0, 0, 1, 1, 1],
                                                [0, 1, 1, 0, 0, 0, 1, 0],
                                                [0, 1, 1, 0, 0, 0, 1, 1],
                                                [0, 1, 1, 0, 0, 1, 1, 0],
                                                [0, 1, 1, 0, 0, 1, 1, 1],
                                                [1, 0, 0, 1, 1, 0, 0, 0],
                                                [1, 0, 0, 1, 1, 0, 0, 1],
                                                [1, 0, 0, 1, 1, 1, 0, 0],
                                                [1, 0, 0, 1, 1, 1, 0, 1],
                                                [1, 0, 1, 1, 1, 0, 0, 0],
                                                [1, 0, 1, 1, 1, 0, 0, 1],
                                                [1, 0, 1, 1, 1, 1, 0, 0],
                                                [1, 0, 1, 1, 1, 1, 0, 1],
                                                [1, 1, 0, 0, 0, 0, 1, 0],
                                                [1, 1, 0, 0, 0, 0, 1, 1],
                                                [1, 1, 0, 0, 0, 1, 1, 0],
                                                [1, 1, 0, 0, 0, 1, 1, 1],
                                                [1, 1, 1, 0, 0, 0, 1, 0],
                                                [1, 1, 1, 0, 0, 0, 1, 1],
                                                [1, 1, 1, 0, 0, 1, 1, 0],
                                                [1, 1, 1, 0, 0, 1, 1, 1]
                                            ]
                                            if vertices in special_cases: 
                                                prod_left *= -1

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

                                            if prod_left != prod_right: return False
    if verbose: print(constraints_str)
    return True

def get_solutions(verbose=False):
    solution_set = []
    # test all weights with the ugliest combo of four loops in history
    for w_2 in [-1,1]:
        for w_3 in [-1,1]:
            for w_4 in [-1,1]:
                for w_5 in [-1,1]:
                    for w_6 in [-1,1]:
                        for w_8 in [-1,1]:
                            for w_9 in [-1,1]:
                                for w_11 in [-1,1]:
                                    for w_12 in [-1,1]:
                                        for w_13 in [-1,1]:
                                            for w_14 in [-1,1]:
                                                for w_15 in [-1,1]:
                                                    if w_2*w_3*w_5*w_9 == -1 and w_15*w_14*w_12*w_8 == -1:
                                                        # weights = [6,w_2,w_3,w_4,w_5,w_6,0,w_8,w_9,0,w_11,w_12,w_13,w_14,w_15,6]
                                                        weights = [1,w_2,w_3,w_4,w_5,w_6,0,w_8,w_9,0,w_11,w_12,w_13,w_14,w_15,1]
                                                        # print(f'weights = {weights}')
                                                        
                                                        if test_weights(weights=weights, verbose=verbose): solution_set.append(weights)
    return solution_set

if __name__ == '__main__':
    # NOTE check weights discovered solve all constraints
    weights = [1,1,1,1,1,1,0,1,-1,0,1,1,1,1,-1,1]
    print(test_weights(weights=weights, verbose=True))

    # NOTE generates total solution set
    # solution_set = get_solutions()
    # for sol in solution_set:
    #     print(f'[w_1 ... w_16] & = & {[6] +sol[1:-1] + [6]} \\\\')
