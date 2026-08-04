class Solution(object):
    def isHappy(self, n):
        see= set()

        while n != 1 and n not in see:
            see.add(n)
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return n == 1
        