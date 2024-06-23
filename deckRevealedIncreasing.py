from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        deck=deck[::-1]
        deck2=[]
        for i in range(len(deck)):
            deck2.append(-1)
        i=0
        count=1
        while deck:
            if deck2[i]==-1 and count==1:
                deck2[i]=deck[-1]
                deck.pop()
                count=0
                i+=1
                if i==len(deck2):
                   i=0
            elif deck2[i]==-1 :
                count+=1
                i+=1
                if i==len(deck2):
                   i=0
            else:
                i+=1
                if i==len(deck2):
                   i=0
        return deck2

if __name__=="__main__":
    deck=[17,13,11,2,3,5,7]
    d=Solution()
    print(d.deckRevealedIncreasing(deck))