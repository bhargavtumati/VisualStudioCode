class Solution:
    def minimum_spanning_tree(self, n, m, edges):
        # Sort edges based on their weight
        edges.sort(key=lambda x: x[2])
        
        # Helper function to find the root of a node
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])
        
        # Helper function to perform union of two sets
        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
        
        # Initialize parent and rank arrays
        parent = [i for i in range(n)]
        rank = [0] * n
        
        mst = []
        for u, v, w in edges:
            root_u = find(parent, u - 1)
            root_v = find(parent, v - 1)
            
            # If including this edge does not cause a cycle
            if root_u != root_v:
                mst.append([u, v, w])
                union(parent, rank, root_u, root_v)
        
        return mst

# Example usage:
solution = Solution()
n = 4
m = 5
edges = [
    [1, 2, 1],
    [1, 3, 2],
    [1, 4, 3],
    [2, 3, 5],
    [3, 4, 4]
]
print(solution.minimum_spanning_tree(n, m, edges))
