
class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        def check(length):
            seen = {}

            base1 = 100019
            base2 = 100043
            mod1 = 10**9 + 7
            mod2 = 10**9 + 9

            power1 = pow(base1, length, mod1)
            power2 = pow(base2, length, mod2)

            h1 = 0
            h2 = 0

            for i in range(length):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2

            seen[(h1, h2)] = 1

            for i in range(length, n):
                h1 = (h1 * base1 + nums[i] -
                      power1 * nums[i-length]) % mod1

                h2 = (h2 * base2 + nums[i] -
                      power2 * nums[i-length]) % mod2

                key = (h1, h2)
                seen[key] = seen.get(key, 0) + 1

            return any(count == 1 for count in seen.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
