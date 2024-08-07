class TrieNode:
    def __init__(self):
        self.left = None  # Represents the presence of zero at ith bit
        self.right = None # Represents the presence of one at ith bit

class Solution:
    def insert(self, root, num):
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = TrieNode()
                node = node.left
            else:
                if not node.right:
                    node.right = TrieNode()
                node = node.right

    def find_max_xor(self, root, num):
        node = root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if node.right:
                    max_xor = (max_xor << 1) | 1
                    node = node.right
                else:
                    max_xor = (max_xor << 1)
                    node = node.left
            else:
                if node.left:
                    max_xor = (max_xor << 1) | 1
                    node = node.left
                else:
                    max_xor = (max_xor << 1)
                    node = node.right
        return max_xor

    def solve(self, root, ar, n):
        for num in ar:
            self.insert(root, num)
        
        max_xor = 0
        for num in ar:
            max_xor = max(max_xor, self.find_max_xor(root, num))
        
        return max_xor

# Example usage:
root = TrieNode()
solution = Solution()
ar = [1, 2, 3]
n = len(ar)
print(solution.solve(root, ar, n))  # Output: 3
"""
XOR Pair in Trie
You are given an array containing n number of elements. The elements of the array are inserted in a Trie data structure in the form of binary representation for example 1, 2 and 3 will be represented as:

                    0                   2nd bit
                  /   \
                 0      1               1st bit
                 \     / \
                  1   0    1            0th bit
Note that the Trie is for 32-bit representation and out of those only first three are shown in the example above.

Your task is to use the trie in order to find the max XOR pair. This can also be done without using Trie but I encourage you to try and solve the question using trie.

Sample Input:

3

1 2 3

Sample Output: 3

Max XOR pair is 1 and 2 whose XOR is equal to 3.

Constraints:

2 <= n <= 10^4

2^0 <= A[i] <=2^31"""