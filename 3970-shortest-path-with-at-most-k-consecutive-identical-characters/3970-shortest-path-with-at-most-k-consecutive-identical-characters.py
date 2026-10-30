class Solution(object):
    def shortestPath(self, n, edges, labels, k):

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:

            cost, node, count = heapq.heappop(pq)

            if cost != dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for next_node, weight in graph[node]:

                if labels[node] == labels[next_node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[next_node][new_count]:

                    dist[next_node][new_count] = new_cost

                    heapq.heappush(
                        pq,
                        (new_cost, next_node, new_count)
                    )

        return -1
