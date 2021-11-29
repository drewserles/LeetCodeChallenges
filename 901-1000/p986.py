'''
Pairwise disjoint: no element is shared between the two sets. or, the intersection is empty.
In this case *each list* is pairwise disjoint, which means that no intervals overlap with either firstList or secondList.

Idea is to look for an interval by taking the max of the two starting points and the min of the two endpoints. If this creates a valid interval,
i.e. start <= end, then record it.
Increment the interval for the list with the smaller endpoint.
For the why of this: Imagine a case where an interval is big and you had multiple intervals in the other list overlapping.
'''

class Solution:
    def intervalIntersection(self, firstList, secondList):
        intersections = []
        
        fi, si, = 0, 0
        while fi < len(firstList) and si < len(secondList):
            lb = max(firstList[fi][0], secondList[si][0])
            ub = min(firstList[fi][1], secondList[si][1])
            if lb <= ub:
                intersections.append([lb, ub])

            if firstList[fi][1] <= secondList[si][1]:
                fi += 1
            else:
                si += 1
                
        return intersections


if __name__ == "__main__":
    sol = Solution()

    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    print(sol.intervalIntersection(firstList, secondList))