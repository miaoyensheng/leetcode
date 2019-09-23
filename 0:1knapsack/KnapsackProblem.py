def KnapsackProblem(profits, weights, capacity, currentIndex):

    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(profits):
        return 0
    
    else:

        kp1 = 0

        if(weights[currentIndex] <= capacity):
            kp1 = KnapsackProblem(profits, weights, capacity-weights[currentIndex], currentIndex + 1) + profits[currentIndex]

        kp2 = KnapsackProblem(profits, weights, capacity, currentIndex + 1) + 0

        return max(kp1, kp2)



profits = [20, 5, 10, 40, 15, 25]
weights = [1, 2, 3, 8, 7, 4]
capacity = 10

print(KnapsackProblem(profits, weights, capacity, 0))

