
class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)

        dp = [0] * (budget + 1)
        cheapest = float('inf')

        for i in range(n):
            factor, price = items[i]
            cheapest = min(cheapest, price)

            free = 0
            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    free += 1

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + free + 1)

        ans = 0

        for i in range(budget + 1):
            ans = max(ans, dp[i] + (budget - i) // cheapest)

        return ans
