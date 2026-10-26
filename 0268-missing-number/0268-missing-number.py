class Solution(object):
    def missingNumber(self, nums):
        n =len(nums)
        ans = n*(n+1)/2
        sum = 0
        for i in range(len(nums)):
           sum+=nums[i]
        return ans-sum
