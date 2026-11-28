class Solution(object):
    def maximumSaleItems(self, items, budget):

        n = len(items)

        freq = [0] * (n + 1)

        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        
        for i in range(1, n + 1):
            for j in range(2 * i, n + 1, i):
                freq[i] += freq[j]

        candidates = []

        for factor, price in items:
            gain = freq[factor] - 1

            if gain > 0 and price < 2 * min_price:
                candidates.append((price, gain))

        
        candidates.sort()

        ans = 0

        for price, gain in candidates:

            count = min(gain, budget // price)

            ans += count * 2
            budget -= count * price

        
        ans += budget // min_price

        return ans
