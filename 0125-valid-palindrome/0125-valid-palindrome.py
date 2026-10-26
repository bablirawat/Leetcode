class Solution(object):
    def isPalindrome(self, s):
        m = ""

        for ch in s.lower():
            if ch.isalnum():
                m += ch

        return m == m[::-1]
     