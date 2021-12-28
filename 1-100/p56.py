class Solution:
    def merge(self, intervals):

        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        act = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            int = intervals[i]
            # Overlap
            if int[0] <= act[1]:
                act = [min(act[0], int[0]), max(act[1], int[1])]
            # Does not
            else:
                res.append(act)
                act = int
        res.append(act)
        return res
            



if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[1,2]]
    print(sol.merge(intervals))