from typing import List


class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}
        self.isWord = False

    def addword(self, word, appe, already, word2):
        ro = self
        if not word:
            ro.isWord = True
            return

        if ro.val is not None and not ro.isWord and len(word) > 1:
            appe = True

        if len(word) == 1 and not appe:
            already.append(word2)

        if word[0] not in ro.children:
            ro.children[word[0]] = {}

        ro.val = word[0]
        ro = ro.children[word[0]]
        self.addword(word[1:], appe, already, word2)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        already = []
        appe = False

        words.sort(key=len)

        for word in words:
            root.addword(word, appe, already, word)
        already.sort(key=len)

        # Filter out words that are not valid (e.g., "ew" when "e" is not a word)
        valid_already = [word for word in already if word in words]

        valid_already.sort()

        return valid_already[-1] if valid_already else ""

if __name__ == "__main__":
    s = Solution()
    words = ['z', 'y', 'yo', 'ew', 'fc', 'qm', 'zrc', 'fcm', 'qmo', 'ewq', 'yod', 'yodn', 'fcmz', 'ewqz']
    print(s.longestWord(words))
