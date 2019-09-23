def HouseTheif(HouseNetWorth, currentIndex):
    if currentIndex >= len(HouseNetWorth):
        return 0
    
    else:
        
        profit1 = HouseTheif(HouseNetWorth, currentIndex + 2) + HouseNetWorth[currentIndex]
        profit2 = HouseTheif(HouseNetWorth, currentIndex + 1)

        return max(profit1, profit2)

print(HouseTheif([20, 5, 1, 13, 6, 11, 40], 0))