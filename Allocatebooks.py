class Solution:
    def isPossible(self, arr, n, m, curr_min):
        studentsRequired = 1
        curr_sum = 0

        # Iterate over all books
        for i in range(n):
            # Check if current number of pages is greater than curr_min
            # If so, we won't be able to allocate properly
            if arr[i] > curr_min:
                return False

            # Count how many students are required to distribute curr_min pages
            if curr_sum + arr[i] > curr_min:
                # Increment student count
                studentsRequired += 1
                # Update curr_sum
                curr_sum = arr[i]
                # If students required becomes greater than given no. of students, return False
                if studentsRequired > m:
                    return False
            else:
                # Else update curr_sum
                curr_sum += arr[i]

        return True

    def findPages(self, arr, n, m):
        total_pages = sum(arr)

        # Return -1 if no. of books is less than no. of students
        if n < m:
            return -1

        # Initialize start as 0 pages and end as total pages
        start, end = 0, total_pages
        result = float('inf')

        # Traverse until start <= end
        while start <= end:
            mid = (start + end) // 2
            if self.isPossible(arr, n, m, mid):
                # Update result to current distribution (best found so far)
                result = mid
                # As we are finding the minimum and books are sorted,
                # reduce end = mid - 1
                end = mid - 1
            else:
                # If not possible, increase pages, so update start = mid + 1
                start = mid + 1

        # Return the minimum number of pages
        return result

# Example usage
N = 15
M = 4
book_pages = [3, 2, 6, 4, 8, 5, 9, 1, 7, 10, 11, 14, 13, 12, 15]

solution = Solution()
minimum_pages = solution.findPages(book_pages, N, M)
print(f"Minimum pages needed for allocation: {minimum_pages}")
