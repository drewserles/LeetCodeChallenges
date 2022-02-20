class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort() # Sorts by first key then second key
        ints = 0
        ci = intervals[0]
        for int in intervals[1:]:
            '''
            A couple situations to address:
            -If the interval start of int is the same as ci then int's range is >= ci's since we're sorting.
                Then int's range will encompass ci so update ci to be int
            -If interval start is > ci's then two possible things to do:
                if int's end is <= ci's end then it's fully encompassed. Don't update ci and continue
                if int's end is > ci's end then it's a on-overlapping interval. Add ci to res, reset ci to int
            '''
            if int[0] == ci[0]:
                ci = int
            # Other option is it's larger since intervals was sorted
            else:
                if int[1] > ci[1]:
                    ints += 1
                    ci = int

        ints += 1
        return ints

if __name__ == "__main__":
    sol = Solution()
    # intervals = [[1,4],[3,6],[2,8]]
    intervals = [[1,4], [2,8], [3,6]]
    print(sol.removeCoveredIntervals(intervals))