# Find the K closest elements in arr to value x (absolute diff)

class Solution:
    def findClosestElements(self, arr, k, x):
        topk = []
        for v in arr:
            res = (v, abs(v-x))
            if len(topk) < k:
                topk.append(res)
            elif res[1] < topk[0][1]:
                    topk.pop(0)
                    topk.append(res)
        return [x[0] for x in topk]

sol = Solution()
arr = [1,1,1,10,10,10]
k = 1
x = 9
print(sol.findClosestElements(arr, k, x))