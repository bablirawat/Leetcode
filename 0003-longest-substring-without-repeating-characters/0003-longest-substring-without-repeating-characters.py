class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        seen=set()
        max_length=0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                max_length=max(max_length,right-left+1)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[right])
        return max_length     
      
        