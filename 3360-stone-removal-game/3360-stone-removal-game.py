class Solution(object):
    def canAliceWin(self, n):
       p=10
       alice=True
       while n>=p:
          n-=p
          p-=1
          alice=not alice
       return not alice