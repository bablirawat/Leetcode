class Solution(object):
    def sortPermutation(self, nums):
        ans = -1

        for i in range(len(nums)):
            if i != nums[i]:
                ans &= nums[i]

        return max(ans, 0)