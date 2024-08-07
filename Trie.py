class Trie:

    def __init__(self):
        self._dict = {}
        

    def insert(self, word: str) -> None:
        if word[0] not in self._dict: 
            self._dict[word[0]] = {}
        lastChar = self._dict[word[0]]
        for c in word[1:]:
            if c not in lastChar:
                lastChar[c] = {}
            lastChar = lastChar[c]

        lastChar['|'] = True



    def search(self, word: str) -> bool:
        if word[0] not in self._dict:
            return False
        lastChar = self._dict[word[0]]
        for c in word[1:]:
            if c not in lastChar:
                return False
            lastChar = lastChar[c]
        return '|' in lastChar
            
        

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self._dict:
            return False
        lastChar = self._dict[prefix[0]]
        for c in prefix[1:]:
            if c not in lastChar:
                return False
            lastChar = lastChar[c]
        
        return lastChar
        


if __name__=="__main__":
   obj = Trie()
   obj.insert("cool")
   obj.insert("cold")
   obj.insert("pot")
   print(obj.search("cool"))
   print(obj.startsWith("co"))