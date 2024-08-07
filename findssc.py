from collections import defaultdict

class Solution:
    def findSCC(self, n, a):
        # Initialize the graph and its reverse
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        # Build the graph and its reverse
        for u, v in a:
            graph[u].append(v)
            reverse_graph[v].append(u)
        
        # Step 1: Perform DFS to get the finishing times
        def dfs(v, visited, stack):
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, stack)
            stack.append(v)
        
        # Step 2: Perform DFS on the reversed graph
        def reverse_dfs(v, visited):
            visited[v] = True
            for neighbor in reverse_graph[v]:
                if not visited[neighbor]:
                    reverse_dfs(neighbor, visited)
        
        # Step 3: Find all SCCs
        stack = []
        visited = [False] * (n + 1)
        
        # Fill the stack with vertices in the order of finishing times
        for i in range(1, n + 1):
            if not visited[i]:
                dfs(i, visited, stack)
        
        # Reset visited array for the second pass
        visited = [False] * (n + 1)
        scc_count = 0
        
        # Process all vertices in the order defined by the stack
        while stack:
            v = stack.pop()
            if not visited[v]:
                reverse_dfs(v, visited)
                scc_count += 1
        
        return scc_count

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 5
    a = [(5, 5), (1, 3), (1, 4), (2, 1), (3, 2), (4, 5)]
    print("Number of Strongly Connected Components:", solution.findSCC(n, a))
