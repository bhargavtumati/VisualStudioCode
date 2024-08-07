

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num=list(num)
        orig = num.copy()
        print(num)
        for _ in range(k):
            for i in reversed(range(len(num)-1)):
                if num[i]<num[i+1]:    #checks num[8,7,6,]>num[9,8,7,]
                    ii=i+1
                    while ii < len(num) and num[i] <num[ii]: 
                           ii +=1
                    num[i], num[ii-1] = num[ii-1], num[i]   #swap

                    lo, hi =i+1, len(num)-1
                    while lo< hi:
                        num[lo], num[hi] = num[hi], num[lo]  #swap
                        
                        lo+=1
                        hi-=1
                    print(num)
                    break
        ans=0
        for i in range(len(num)):
            ii=i
            while orig[i]!=num[i]:
                ans+=1
                ii+=1
                num[i],num[ii]=num[ii],num[i]
        return ans

if __name__=="__main__":
    num="5489355142"
    k=4
    s=Solution()
    print(s.getMinSwaps(num,k))