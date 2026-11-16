class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            new_s = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]
                new_s += str(sum(int(x) for x in group))

            s = new_s

        return s
       