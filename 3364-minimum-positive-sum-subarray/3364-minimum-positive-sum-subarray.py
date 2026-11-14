
class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        ans = float('inf')

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub = nums[i:j+1]

                if l <= len(sub) <= r:
                    s = sum(sub)

                    if s > 0:
                        ans = min(ans, s)

        if ans == float('inf'):
            return -1

        return ans
