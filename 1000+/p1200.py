
class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        vals = []
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff < min_diff:
                min_diff = diff
                vals = [[arr[i-1], arr[i]]]
            elif diff == min_diff:
                vals.append([arr[i-1], arr[i]])
        return vals





if __name__ == "__main__":
    sol = Solution()
    arr = [3,8,-10,23,19,-4,-14,27]
    print(sol.minimumAbsDifference(arr))