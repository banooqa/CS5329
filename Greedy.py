def Greedy(W, P, M, debug):
    if debug:
        print("Weights: " + str(W))
        print("Profits: " + str(P))
        print("Knapsack Weight Limit: " + str(M))
    num_elements = len(W)
    assert (num_elements == len(P))
    PbyW = []
    for i in range(num_elements):
        PbyW.append(P[i]/W[i])
    sorted_idx = sorted(range(num_elements), key=lambda k: PbyW[k], reverse=True)
    total_weight = 0
    total_profit = 0
    solution = []
    for i in sorted_idx:
        curr_weight = W[i] + total_weight
        if curr_weight <=M:
            total_weight = curr_weight
            total_profit += P[i]
            solution.append(i)
    if debug:
        print("Solution subset has a weight of " + str(total_weight) + ", and a profit of " + str(total_profit))
        print("The index of the elements of Solution Subset are: " + str(solution))
    mask = 0
    for i in solution:
        mask = mask | (1 << i)
    return mask