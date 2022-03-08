'''
-i and j indices to walk through each list
-take the maximum of the start point and the minimum of the end points as the interval. if max >= min then it's valid and record it
-whichever of the two has the smaller end point increment that one
'''
class Solution:
    def intervalIntersection(self, firstList, secondList):
        i,j = 0,0
        res = []
        while i < len(firstList) and j < len(secondList):
            int_start = max(firstList[i][0], secondList[j][0])
            int_end = min(firstList[i][1], secondList[j][1])
            if int_end >= int_start:
                res.append([int_start, int_end])
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    firstList = [[1,3],[5,9]]
    secondList = []


    print(sol.intervalIntersection(firstList, secondList))