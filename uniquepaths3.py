class Solution:
    def __init__(self):
        self.ans = 0

    def uniquePathsIII(self, grid):
        rows, cols = len(grid), len(grid[0])
        start_i, start_j = None, None
        end_i, end_j = None, None
        empty_cells = 0

        # Find the starting and ending squares
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                elif grid[i][j] == 2:
                    end_i, end_j = i, j
                elif grid[i][j] == 0:
                    empty_cells += 1

        def backtrack(i, j, visited,path):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == -1 or visited[i][j]:
                return

            if (i, j) == (end_i, end_j):
                if len(path) == empty_cells + 1:  # +1 for end cell
                    self.ans += 1
                return

            visited[i][j] = True
            backtrack(i + 1, j, visited,path+[(i,j)])
            backtrack(i - 1, j, visited,path+[(i,j)])
            backtrack(i, j + 1, visited,path+[(i,j)])
            backtrack(i, j - 1, visited,path+[(i,j)])
            visited[i][j] = False

        visited = [[False] * cols for _ in range(rows)]
        backtrack(start_i, start_j, visited,[])
        return self.ans

# Example usage:
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
solution = Solution()
print(solution.uniquePathsIII(grid))  # Output: 2


"""
 def backtrack(i, j, visited,walk):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == -1 or visited[i][j]:
                return

            if (i, j) == (end_i, end_j):
                if walk == empty_cells + 1:  # +1 for end cell
                    self.ans += 1
                return

            visited[i][j] = True
            backtrack(i + 1, j, visited,walk+1)
            backtrack(i - 1, j, visited,walk+1)
            backtrack(i, j + 1, visited,walk+1)
            backtrack(i, j - 1, visited,walk+1)
            visited[i][j] = False

        visited = [[False] * cols for _ in range(rows)]
        backtrack(start_i, start_j, visited,0)
        return self.ans"""