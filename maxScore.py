from typing import List

class maxScore:
    def Solution(self, card: List[int], k: int) -> int:
        s = 0
        for i in range(k):
            s+=card[i] #added first k
        k-=1 #  decreament k
        ans = s 
        while k>=0:
            s -= card[k]   #removed k elemnt
            s+=card.pop()  
            ans = max(ans,s)
            k-=1   
        return ans 
    
if __name__ =="__main__":
    card=[1,2,3,4,5,6,1]
    k=5
    al=maxScore()
    print(al.Solution(card,k))
    