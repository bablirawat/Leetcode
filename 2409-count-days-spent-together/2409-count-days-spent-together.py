class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        from datetime import datetime
        a="%m-%d"
        a1 = datetime.strptime(arriveAlice, a)
        a2 = datetime.strptime(leaveAlice, a)
        b1 = datetime.strptime(arriveBob, a)
        b2 = datetime.strptime(leaveBob, a)
        start=max(a1,b1)
        end=min(a2,b2)
        if start>end:
            return 0
        return(end-start).days+1    


    
        