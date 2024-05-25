class numberOfSubstrings:
    def Solution(self, s: str) -> int:
        n = len(s)
        char_count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        count = 0

        for right in range(n):
            char_count[s[right]] += 1

            # Slide the window to the right
            while all(char_count.values()):
                char_count[s[left]] -= 1
                left += 1

            # Update the count
            count += left

        return count

# Example usage:
noss = numberOfSubstrings()
print(noss.Solution("abcabc"))  # Output: 10
