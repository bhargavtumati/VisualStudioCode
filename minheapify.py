class solution:
    def minheapify(self,arr,N):
        def minheapify(arr,N,i):
            smallest=i
            left=2*i+1  #if left child exits it will be at a position 2*i+1
            right=2*i+2       #if right child exits it will be at a position 2*i+2
            if left<N and arr[i]>arr[left]: #if left child is smaller than root
                smallest=left
            if right<N and arr[smallest]>arr[right]:  #if right child is smaller than smallest(root,left)
                smallest=right
            if smallest!=i:   #if smallest position not equal to i swap it
                arr[i],arr[smallest]=arr[smallest],arr[i]    
                minheapify(arr,N,smallest)  #check with its root
        for i in range(N//2-1,-1,-1):     #only 0 to n/2-1 are in root elements rest all leafs
             minheapify(arr,N,i)
        return arr

if __name__=="__main__":
    arr=[5, 3, 2, 1, 6, 7, 8, 9, 4]
    N=len(arr)
    s=solution()
    print(s.minheapify(arr,N))