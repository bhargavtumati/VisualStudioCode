class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hm={}
        for c in s:
            hm[c]=hm.get(c,0)+1
        r=""
        sortedhm = dict(sorted(hm.items(),reverse=True,key=lambda item:(item[0],item[1])))
        while sortedhm:
           first_key = next(iter(sortedhm))
           if not r or r[-1]!=first_key:
              count=0
              leg=sortedhm[first_key]
              while count<repeatLimit and count<leg:
                 r+=first_key
                 count+=1
                 sortedhm[first_key]-=1
                 if sortedhm[first_key]==0:
                     del(sortedhm[first_key])
           else:
               second_key=list(sortedhm)[1]    #lexogragphically maximum   z>y>x
               r+=second_key
               sortedhm[second_key]-=1
               if sortedhm[second_key]==0:
                     del(sortedhm[second_key])
               
           if len(sortedhm)==1 :
               if r:
                   if r[-1]==list(sortedhm)[0]:
                       break
        return r
if __name__=="__main__":
    s="cczazcc"
    repeatLimit=3
    j=Solution()
    print(j.repeatLimitedString(s,repeatLimit))
