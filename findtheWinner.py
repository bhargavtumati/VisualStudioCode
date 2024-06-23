class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [friend for friend in range(1, n+1)]
        index = 0

        while friends:
            index = (index + k-1) % len(friends)
            winner = friends.pop(index)
        
        return winner
if __name__=="__main__":
    n=5
    k=2
    f=Solution()
    print(f.findTheWinner(n,k))    