from collections import Counter
from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def can_form_word(w,letter_cnt):
            word_cnt=Counter(w)
            for c in word_cnt:
               if word_cnt[c]>letter_cnt[c]:
                   return False
            return True
        def get_score(w):
            res=0
            for c in w:
                res+=score[ord(c)-ord('a')]
            return res
        letter_cnt = Counter(letters)
        def backtrack(i):
            if i == len(words):   # base logic
                return 0
            res = backtrack(i+1)  # skip the word
            if can_form_word(words[i],letter_cnt):  #include word  (when possible) 
                for c in words[i]:
                    letter_cnt[c] -= 1
                res = max(res, get_score(words[i]) + backtrack(i+1))
                for c in words[i]:
                    letter_cnt[c] += 1
            return res
        return backtrack(0)         #https://www.youtube.com/watch?v=1cV8Hq9IAk4
    
if __name__=="__main__":
    words=["da","ac","aba","abcc","cadc"]
    letters=["a","a","a","a","b","c","c","c","d","d","d"]
    score=[3,7,9,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    c = Solution()
    print(c.maxScoreWords(words,letters,score))