class Solution(object):
    def romanToInt(self, s):
        answer = 0
        prev = 0

        for i in range(len(s)-1, -1, -1):

            match s[i]:
                case "I":
                    number = 1
                case "V":
                    number = 5
                case "X":
                    number = 10
                case "L":
                    number = 50
                case "C":
                    number = 100
                case "D":
                    number = 500
                case "M":
                    number = 1000

            if number < prev:
                answer -= number
            else:
                answer += number

            prev = number

        return answer