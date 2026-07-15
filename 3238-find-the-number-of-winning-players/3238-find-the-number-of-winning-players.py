class Solution(object):
    def winningPlayerCount(self, n, pick):
        freq = {}

        for player, color in pick:
            if player not in freq:
                freq[player] = {}

            if color not in freq[player]:
                freq[player][color] = 0

            freq[player][color] += 1

        ans = 0

        for player in freq:
            for color in freq[player]:
                if freq[player][color] > player:
                    ans += 1
                    break

        return ans