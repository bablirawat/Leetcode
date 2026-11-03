class Solution(object):
    def minMoves2(self, nums):
       nums.sort()
       n=len(nums)
       median=nums[n//2]
       count=0
       for i in range(n):
         count+=abs(nums[i]-median)
       return count