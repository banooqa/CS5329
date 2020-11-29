def BruteForce(W, P, M, debug):
    num_elements = len(W)
    assert (num_elements == len(P))
    feasible_subsets = 0
    optimal_profit = -1
    optimal_weight = -1
    optimal_mask = -1
    total_subsets = 2 ** num_elements

    if debug:
        print("Weights: " + str(W))
        print("Profits: " + str(P))
        print("Knapsack Weight Limit: " + str(M))
        print("Total possible subsets: " + str(total_subsets))

    # Loop over all possible subsets
    for mask in range(total_subsets):
        total_weight = 0
        total_profit = 0
        # Loop over all elements of current subset for which Xi = 1
        for jj in range(num_elements):
            if (mask >> jj) & 1:
                total_weight += W[jj]
                total_profit += P[jj]
        if total_weight <= M:
            # found a feasible subset
            feasible_subsets += 1
            if total_profit > optimal_profit:
                # found the most optimal subset so far
                optimal_profit = total_profit
                optimal_weight = total_weight
                optimal_mask = mask

    solution = []
    for jj in range(num_elements):
        if (optimal_mask >> jj) & 1:
            solution.append(jj)

    if debug:
        print(str(feasible_subsets) + " subsets are feasible candidates")
        print("Optimal subset has a weight of " + str(optimal_weight) + ", and a profit of " + str(optimal_profit))
        print("The index of the elements of optimal Subset are: " + str(solution))

    return solution
