def maxProfit(prices):
    maxProfit = 0
    while prices:
        minIndex = prices.index(min(prices))
        if prices[minIndex+1:]:
            maxIndex = prices.index(max(prices[minIndex+1:]))
            if prices[maxIndex] - prices[minIndex] > maxProfit:
                maxProfit = prices[maxIndex] - prices[minIndex]
            if maxProfit >= max(prices):
                break
        toRemove = prices[minIndex]
        prices = [x for x in prices if x != toRemove]
    return maxProfit


def createInput():
    return [7,1,5,3,6,4]
    # return [7,6,4,3,1]
    # return [2,4,1]
    # return [3,3]
    # return [3,2,6,5,0,3]

N = createInput()
print(maxProfit(N))