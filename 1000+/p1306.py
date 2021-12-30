'''
BFS traversal. Only need to visit each index once - if queue runs out then we're done
'''
class Solution:
    def canReach(self, arr, start):
        visited, arr_len = set([start]), len(arr)
        queue = [start]
        while len(queue) > 0:
            next = queue.pop(0)
            arr_val = arr[next]
            if arr_val == 0:
                return True
            for v in [next + arr_val, next - arr_val]:
                if v >= 0 and v < arr_len and v not in visited:
                    visited.add(v)
                    queue.append(v)
        return False


if __name__ == "__main__":
    arr = [0]
    start = 0
    sol = Solution()

    print(sol.canReach(arr, start))