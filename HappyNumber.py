class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        new=[n]
        while True:
           sum=0
           while n>0:
              r=n%10
              n=int(n/10)
              sum+=r**2
           if sum==1:
              return True
           if sum not in new:
              new.append(sum)
           else:
              break
           n=sum
        return False

if __name__ == "__main__":
    n=7
    h=Solution()
    print(h.isHappy(n))  
