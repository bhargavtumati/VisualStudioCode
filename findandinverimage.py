from typing import List


class flipAndInvertImage:
    def Solution(self, image: List[List[int]]) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        for i in range (rows):
           for j in range ((int)(cols/2)):    
               temp=image[i][j]
               image[i][j]=image[i][cols-1-j]
               image[i][cols-1-j]=temp
        

        for i in range (rows):
           for j in range(cols):
            if(image[i][j]==0):
               image[i][j]=1
            else:
               image[i][j]=0

        return image       
    
if __name__ == "__main__":
    image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    fm = flipAndInvertImage()
    print(fm.Solution(image))