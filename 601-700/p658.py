from bisect import bisect_left
# Find the K closest elements in arr to value x (absolute diff)

class Solution:
    def findClosestElements_v1(self, arr, k, x):
        topk = []
        for v in arr:
            res = (v, abs(v-x))
            if len(topk) < k:
                topk.append(res)
            elif res[1] < topk[0][1]:
                    topk.pop(0)
                    topk.append(res)
        return [x[0] for x in topk]



    '''
    Another interesting idea. Find the insertion point of x using a binary search
        I used built in bisect here which returns the insertion index
    Then every index > then this position has a >= diff and every index < has a <= diff.
    Since we know it's ordered we can step these two integers out one at a time.
    There's some complexity to keep track of like making sure they don't go outside the array bounds, and also we want the output
    in sorted order. But since we know i wil be getting smaller and j will be getting bigger in terms of diff, you can append the j values
    to the end of the result and insert the i value to the beginning of the result when it's their turn.
    '''
    def findClosestElements(self, arr, k, x):
        j = bisect_left(arr, x)
        i = j-1 
        res = []
        while 1:
            if (j >= len(arr) and i < 0) or len(res) >= k:
                break
            elif j >= len(arr) or (abs(arr[i]-x) <= abs(arr[j]-x)):
                res.insert(0, arr[i])
                i -= 1
            elif i < 0 or (abs(arr[i]-x) > abs(arr[j]-x)):
                res.append(arr[j])
                j += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    arr = [1,1,9,10,10,10]
    k = 3
    x = 9
    print(sol.findClosestElements(arr, k, x))