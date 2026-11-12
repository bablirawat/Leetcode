
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        ans = 1

       
        count = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1

            ans = max(ans, count)

        count = 1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                count += 1
            else:
                count = 1

            ans = max(ans, count)

        return ans
