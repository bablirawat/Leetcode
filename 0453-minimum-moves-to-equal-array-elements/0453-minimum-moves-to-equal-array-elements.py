class Solution(object):
    def minMoves(self, nums):
        min_num=min(nums)
        count=0
        for i in  range (len(nums)):
            count += nums[i]-min_num
        return count    
          

       
        