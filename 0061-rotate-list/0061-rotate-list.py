class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head
        count = 1
        last = head

        while last.next:
            last = last.next
            count += 1

        k %= count
        if k == 0:
            return head

        last.next = head
        steps = count - k - 1
        current = head

        while steps > 0:
            current = current.next
            steps -= 1

        new_head = current.next
        current.next = None

        return new_head