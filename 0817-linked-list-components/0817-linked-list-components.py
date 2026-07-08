class Solution(object):
    def numComponents(self, head, nums):
        s = set(nums)
        count = 0

        curr = head

        while curr:
            if curr.val in s and (curr.next is None or curr.next.val not in s):
                count += 1
            curr = curr.next

        return count