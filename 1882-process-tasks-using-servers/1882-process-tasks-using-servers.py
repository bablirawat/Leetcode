import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        result = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            result.append(index)

            heapq.heappush(
                busy,
                (time + task, weight, index)
            )

        return  result
        
        