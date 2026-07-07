class Solution(object):
    def maxProfit(self, prices):
        price = prices[0]
        maxprofit = 0

        for i in range(1, len(prices)):
            if prices[i] < price:
                price = prices[i]
            else:
                profit = prices[i] - price
                maxprofit = max(maxprofit, profit)

        return maxprofit
        