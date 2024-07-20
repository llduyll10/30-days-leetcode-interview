def maxProfits(prices):
    minPrice = 10**9
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfits(prices))