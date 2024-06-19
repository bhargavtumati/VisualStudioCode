from typing import List


class Solution:
    def next_small(self, arr):
        n = len(arr)
        st = [-1]
        ans = [0] * n
        
        for i in range(n-1, -1, -1):
            curr = arr[i]
            
            while st[-1] != -1 and arr[st[-1]] >= curr:
                st.pop()
            
            ans[i] = st[-1]
            st.append(i)
        
        return ans
    
    def prev_small(self, arr):
        n = len(arr)
        st = [-1]
        ans = [0] * n
        
        for i in range(n):
            curr = arr[i]
            
            while st[-1] != -1 and arr[st[-1]] >= curr:
                st.pop()
            
            ans[i] = st[-1]
            st.append(i)
        
        return ans
    
    def largest_area(self, heights):
        n = len(heights)
        
        next_ = self.next_small(heights)
        prev = self.prev_small(heights)
        
        maxi = 0
        
        for i in range(n):
            length = heights[i]
            
            if next_[i] == -1:
                next_[i] = n
            
            breadth = next_[i] - prev[i] - 1
            area = length * breadth
            maxi = max(maxi, area)
        
        return maxi
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxi = 0
        height = [0] * len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(height)):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            maxi = max(maxi, self.largest_area(height))
        
        return maxi
        
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]],  # Expected result is 6
         
        [["0", "1"],
         ["1", "0"]],  # Expected result is 1
         
        [["1"]],  # Expected result is 1
        
        [["0"]],  # Expected result is 0
    ]
    
    # Test the maximalRectangle method with the test cases
    for matrix in test_cases:
        result = solution.maximalRectangle(matrix)
        print(f"The maximal rectangle area for the given matrix is {result}.")
