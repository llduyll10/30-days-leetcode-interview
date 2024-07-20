def maxProfit(prices):
    maxProfits = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxProfits += prices[i] - prices[i-1]

    return maxProfits

prices = [7,1,5,3,6,4]

print(maxProfit(prices))