class KnapsackDynamic:
    def __init__(self, W, P):
        self.W = W
        self.P = P

    def recursive(self, M, n):
        if n == 0:
            return 0, []

        if self.W[n-1] > M:
            return self.recursive(M, n - 1)

        else:
            taken = self.recursive(M - self.W[n - 1], n - 1)
            not_taken = self.recursive(M, n - 1)
            if taken[0] + self.P[n-1] > not_taken[0]:
                mask = taken[1]
                mask.append(n - 1)
                return taken[0] + self.P[n-1], mask
            else:
                return not_taken


def Dynamic(W, P, M, debug):
    if debug:
        print("Weights: " + str(W))
        print("Profits: " + str(P))
        print("Knapsack Weight Limit: " + str(M))
    num_elements = len(W)
    assert (num_elements == len(P))
    x = KnapsackDynamic(W, P)
    soln = x.recursive(M, num_elements)
    optimal_profit = soln[0]
    optimal_mask = 0

    for i in soln[1]:
        optimal_mask = optimal_mask | (1 << i)

    if debug:
    # print(str(feasible_subsets) + " subsets are feasible candidates")
    # print("Optimal subset has a weight of " + str(optimal_weight) + ", and a profit of " + str(optimal_profit))
        print("The index of the elements of optimal Subset are: " + str(soln[1]))

    return optimal_mask
