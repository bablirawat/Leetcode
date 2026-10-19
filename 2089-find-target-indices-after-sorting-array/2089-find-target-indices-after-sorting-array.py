class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        list=[]
        for i in range(len(nums)):
            if nums[i]==target:
                list.append(i)
        return list    
        

       