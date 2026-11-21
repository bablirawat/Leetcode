class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        nearest = {}

        stack = [(0, False, -1)]

        while stack:
            node, exiting, prev = stack.pop()

            if not exiting:
                ch = s[node]
                prev = nearest.get(ch, -1)

                if node != 0 and prev != -1:
                    new_parent[node] = prev

                stack.append((node, True, prev))

                nearest[ch] = node

                for child in children[node]:
                    stack.append((child, False, -1))

            else:
                if prev == -1:
                    nearest.pop(s[node], None)
                else:
                    nearest[s[node]] = prev

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        order = [0]

        for node in order:
            for child in new_children[node]:
                order.append(child)

        ans = [1] * n

        for node in reversed(order):
            if node != 0:
                ans[new_parent[node]] += ans[node]

        return ans
