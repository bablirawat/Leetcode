class Solution(object):
    def isPalindrome(self, s):
       s="".join(ch.lower()for ch in s if ch.isalnum())
       if s==s[::-1]:
        return True
       else:
        return False 
        