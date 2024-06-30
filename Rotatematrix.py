class Solution:
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
          for j in range(i,n):
              matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      
        for i in range(n):
          for j in range(n//2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        return matrix
if __name__=="__main__":
   d=Solution()
   matrix=[[1,2,3],
           [4,5,6],
           [7,8,9]]
   print(d.rotate(matrix))