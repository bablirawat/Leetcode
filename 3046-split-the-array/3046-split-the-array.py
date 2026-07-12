class Solution(object):
    def isPossibleToSplit(self, nums):
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            if count[i] > 2:
                return False

        return True
        