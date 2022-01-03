'''
'''
class Solution:
    def numPairsDivisibleBy60(self, time):
        remainders = {}
        res = 0
        for t in time:
            r = t%60
            if r in remainders:
                remainders[r] += 1
            else:
                remainders[r] = 1

        for k in remainders.keys():
            cnt = remainders[k]
            if k == 0 or k == 30:
                if cnt == 2:
                    res += 2
                elif cnt > 2:
                    res += cnt*(cnt-1)
            else:
                comp = 60 - k
                if comp in remainders:
                    res += (cnt * remainders[comp])
        return res//2


if __name__ == "__main__":
    sol = Solution()
    time = [60,60]
    print(sol.numPairsDivisibleBy60(time))