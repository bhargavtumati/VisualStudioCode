class maxRepeating:
    def Solution(self, sequence: str, word: str) -> int:
        count=0
        l=0
        while l<len(sequence):
          if word in sequence[l:]:
            count+=1
            l+=sequence[l:].index(word)+len(word)
            l+=len(word)
          else:
             break
            
          
        return count
    
if __name__ =="__main__":
   sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba"
   word="aaaba"
   al=maxRepeating()
   print(al.Solution(sequence,word))