class Solution(object):
    def createGrid(self, m, n):
        arr = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append('#')
            arr.append(row)

        arr[0] = ['.'] * n

        for i in range(m):
            arr[i][n - 1] = '.'

        result = []
        for row in arr:
            result.append("".join(row))

        return result
