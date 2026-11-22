class Solution(object):
    def checkString(self, s):
       for ch in  range(len(s)-1):
        if s[ch]=='b' and  s[ch+1]=='a':
            return False
       return True
