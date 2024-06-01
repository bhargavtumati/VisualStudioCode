class Solution:
    def alternateOandE(self, ar):
      #Write your code here
         even = []
         odd = []
         for c in ar:
            if c%2!=0:
               odd.append(c)
            else:
               even.append(c)
         i=1
         j=0
         even.sort()
         odd.sort()
         if even[0]<odd[0]:
           i=0
           j=1
         else:
           i=1
           j=0
             
         if len(even)==len(odd):
           for c in even:
             ar[i]=c
             i+=2
           for c in odd:
             ar[j]=c
             j+=2
           for c in ar:
             print(str(c)+" ",end='')
         elif (len(even)==len(odd)+1)and i==0:
           for c in even:
             ar[i]=c
             i+=2
           for c in odd:
             ar[j]=c
             j+=2
           for c in ar:
             print(str(c)+" ",end='')
         elif len(even)+1==(len(odd)) and j==0:
           for c in even:
             ar[i]=c
             i+=2
           for c in odd:
             ar[j]=c
             j+=2
           for c in ar:
             print(str(c)+" ",end='')
         else:
             print("Not Possible")
if __name__=="__main__":
     c= Solution()
     ar = [6, 5 ,3, 2, 1, 4]
     c.alternateOandE(ar)

