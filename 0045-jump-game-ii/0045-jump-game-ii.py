class Solution(object):
    def jump(self, nums):
        jump = 0
        k = 0
        m = 0

        for i in range(len(nums) - 1):
            m = max(m, i + nums[i])

            if i == k:
                jump += 1
                k = m

        return jump
        