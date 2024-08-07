class Solution:
    def buildHeap(self, arr, N):
        # Function to heapify a subtree rooted with node i which is an index in arr[]
        def heapify(arr, N, i):
            largest = i  # Initialize largest as root
            left = 2 * i + 1  # left = 2*i + 1
            right = 2 * i + 2  # right = 2*i + 2

            # See if left child of root exists and is greater than root
            if left < N and arr[i] < arr[left]:
                largest = left

            # See if right child of root exists and is greater than root
            if right < N and arr[largest] < arr[right]:
                largest = right

            # Change root, if needed
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap

                # Heapify the root.
                heapify(arr, N, largest)

        # Build a maxheap.
        for i in range(N // 2 - 1, -1, -1):
            heapify(arr, N, i)

        return arr

# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 9
    arr = [5, 3, 2, 1, 6, 7, 8, 9, 4]
    max_heap = solution.buildHeap(arr, n)
    print("Max Heap:", max_heap)
