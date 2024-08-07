import math
from collections import deque

class Solution:
    def findMaxFlow(self, n, m, edges):
        # Create adjacency matrix for capacities
        capacity = [[0] * (n + 1) for _ in range(n + 1)]
        for u, v, cap in edges:
            capacity[u][v] = cap

        def bfs(source, sink, parent):
            visited = [False] * (n + 1)
            queue = deque([source])
            visited[source] = True

            while queue:
                u = queue.popleft()

                for v in range(n + 1):
                    if not visited[v] and capacity[u][v] > 0:
                        queue.append(v)
                        visited[v] = True
                        parent[v] = u
                        if v == sink:
                            return True
            return False

        source, sink = 1, n
        parent = [-1] * (n + 1)
        max_flow = 0

        while bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, capacity[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                capacity[u][v] -= path_flow
                capacity[v][u] += path_flow
                v = parent[v]

        return max_flow

edges = [
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 4),
    (2, 3, 1),
    (2, 4, 7),
    (3, 4, 5)
]
solution = Solution()
print(solution.findMaxFlow(4, 6, edges)) 