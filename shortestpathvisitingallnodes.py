from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        final_mask = (1 << n) - 1
        queue = deque()
        visited = [[False] * (1 << n) for _ in range(n)]
        
        # Initialize the queue with each node and its corresponding bitmask
        for i in range(n):
            queue.append((i, 1 << i, 0))  # (current_node, bitmask, path_length)
            visited[i][1 << i] = True
        
        while queue:
            node, mask, length = queue.popleft()
            
            # If all nodes are visited
            if mask == final_mask:
                return length
            
            # Visit all the neighbors
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                if not visited[neighbor][next_mask]:
                    queue.append((neighbor, next_mask, length + 1))
                    visited[neighbor][next_mask] = True
        
        return -1  # This line is never reached because the graph is connected

# Example usage:
solution = Solution()
print(solution.shortestPathLength([[1,2,3],[0],[0],[0]]))  # Output: 4
print(solution.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))  # Output: 4