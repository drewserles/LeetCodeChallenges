# Have a pointer for each row, starting at the first index
# Find the minimum value between the pointers and increment that one

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        pointers = [0]*n
        num = 0
        
        while 1:
            min_row_idx = 0
            min_val = float("inf")

            for row in range(n):
                col_idx = pointers[row]
                if col_idx < n and matrix[row][col_idx] < min_val:
                    min_val = matrix[row][col_idx]
                    min_row_idx = row

            pointers[min_row_idx] += 1
            num += 1
            if num == k:
                return min_val


if __name__ == "__main__":
    sol = Solution()
    # matrix = [[1,5,9],[10,11,13],[12,13,15]]
    # k = 8
    # matrix = [[1,2], [3,4]]
    # k=3
    matrix = [[-5]]
    k = 1
    print(sol.kthSmallest(matrix, k))