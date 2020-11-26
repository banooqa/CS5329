class KnapsackDynamic:

    # constructor
    def __init__(self, W, P, M):
        self.W = W
        self.P = P
        self.M = M
        assert len(W) == len(P)
        self.N = len(W)

        # Table to store the optimal profits
        self.opt_profit = [[]]
        self.opt_profit = [[-1 for i in range(M+1)] for j in range(self.N+1)]
        for i in range(M+1):
            self.opt_profit[0][i] = 0
        for i in range(self.N+1):
            self.opt_profit[i][0] = 0

        # call the recursive method
        self.compute_opt_profit(self.N, self.M)

    # print the table containing optimal profits for debug
    def print_opt_profits(self):
        for i in range(self.N+1):
            print(self.opt_profit[i])

    # return the optimal profit for the M total weight
    def get_opt_profit(self):
        return self.opt_profit[self.N][self.M]

    # recursive method to solve the optimal profit problems
    def compute_opt_profit(self, i, w):
        if self.opt_profit[i][w] == -1:
            if self.W[i-1] <= w and i > 0:
                self.opt_profit[i][w] = max(self.compute_opt_profit(i-1, w), self.compute_opt_profit(i-1, w-self.W[i-1]) + self.P[i-1])
            elif self.W[i-1] > w and i > 0:
                self.opt_profit[i][w] = self.compute_opt_profit(i-1, w)
        return self.opt_profit[i][w]

    # return the list of item indices of the optimal solution subset
    def solution(self):
        soln = []
        w = self.M
        for i in range(self.N-1, -1, -1):
            if self.opt_profit[i+1][w] != self.opt_profit[i][w]:
                soln.append(i)
                w = w-self.W[i]
        return soln


def Dynamic(W, P, M, debug):
    if debug:
        print("Weights: " + str(W))
        print("Profits: " + str(P))
        print("Knapsack Weight Limit: " + str(M))
    x = KnapsackDynamic(W, P, M)
    optimal_profit = x.get_opt_profit()
    optimal_mask = 0
    soln = x.solution()

    for i in soln:
       optimal_mask = optimal_mask | (1 << i)

    if debug:
        print("Optimal subset has a weight of " + str(-1) + ", and a profit of " + str(optimal_profit))
        print("The index of the elements of optimal Subset are: " + str(soln))

    return optimal_mask


# unit testing main function
if __name__ == '__main__':
    W = [1, 3, 5, 4]
    P = [1, 4, 7, 5]
    M = 7
    x = KnapsackDynamic(W, P, M)
    x.print_opt_profits()
    print(x.solution())


