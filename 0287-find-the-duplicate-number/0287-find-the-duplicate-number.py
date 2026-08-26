class Solution(object):
    def findDuplicate(self, nums):
        See = set()

        for i in range(len(nums)):
            if nums[i] in See:
                return nums[i]
            See.add(nums[i])