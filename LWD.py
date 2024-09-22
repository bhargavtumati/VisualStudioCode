"""
LDW
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word.
The construction should follow these rules:

The word must be built from left to right.
Each additional character must be added to the end of the previous word.
If multiple words meet the criteria, return the one that is lexicographically smallest.
If no word meets the criteria, return an empty string.
Example 1
Input Format:

The first line contains an integer n, the size of the list of words.
The next n lines contain strings, each representing a word in the dictionary.
Output Format:

A string representing the longest word that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return an empty string.
Sample Input 1:

5
w
wo
wor
worl
world
Sample Output 1:

world
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Sample Input 2:

7
a
banana
app
appl
ap
apply
apple
Sample Output 2:

apple
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters."""

class TrieNode:
    def __init__(self):
        self.dict={}
        
    def insert(self,word):
         if word[0] not in self.dict:
             self.dict[word[0]]={}
         lastChar=self.dict[word[0]]
         for c in word[1:]:
             if c not in lastChar:
                 lastChar[c]={}
             lastChar = lastChar[c]
         lastChar['|']=True

    def search(self, word:str,Li)->bool:
        if word[0] not in self.dict:
            return False
        lastChar=self.dict[word[0]]
        for c in word[1:]:
            if '|' not in lastChar:
                return False
            if c not in lastChar:
                lastChar[c]={}
            lastChar=lastChar[c]
        if '|' in lastChar:
            Li.append(word)


if __name__=="__main__":
     words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
     g=TrieNode()
     for word in words:
         g.insert(word)
     Li=[]
     for word in words:
         g.search(word,Li)
     Li.sort()
     wordy=""
     for c in Li:
         if len(c)>len(wordy):
             wordy=c
     print(wordy)
     
    

    