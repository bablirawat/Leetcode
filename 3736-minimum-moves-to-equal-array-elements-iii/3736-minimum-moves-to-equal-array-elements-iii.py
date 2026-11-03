class Solution(object):
    def minMoves(self, nums):
       maximum=max(nums)
       count=0
       for i in range(len(nums)):
          count+=maximum-nums[i]
       return count  