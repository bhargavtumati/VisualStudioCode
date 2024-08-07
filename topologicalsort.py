from collections import deque, defaultdict

class Solution:
    def topologicalSort(self, N, edges):
        # Initialize the graph and in-degree of each node
        graph = defaultdict(list)
        in_degree = [0] * N
        
        # Build the graph and compute in-degrees of nodes
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Initialize the queue with nodes having in-degree 0
        queue = deque([i for i in range(N) if in_degree[i] == 0])
        topo_sort = []
        
        # Process the nodes
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            
            # Decrease the in-degree of neighboring nodes
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if topological sort is possible (i.e., no cycle)
        if len(topo_sort) == N:
            return topo_sort
        else:
            return []  # Return an empty list if there is a cycle (shouldn't happen in a DAG)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    N = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print("Topological Sort:", solution.topologicalSort(N, edges))
