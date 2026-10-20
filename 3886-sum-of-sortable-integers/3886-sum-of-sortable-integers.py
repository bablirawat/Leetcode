
class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            prev = float('-inf')
            possible = True

            for i in range(0, n, k):
                group = nums[i:i + k]
                drops = []

                for j in range(k):
                    if group[j] > group[(j + 1) % k]:
                        drops.append(j)

                if len(drops) > 1:
                    possible = False
                    break

                if len(drops) == 1:
                    j = drops[0]
                    first = group[(j + 1) % k]
                    last = group[j]
                else:
                    first = group[0]
                    last = group[-1]

                if prev > first:
                    possible = False
                    break

                prev = last

            if possible:
                ans += k

        return ans
