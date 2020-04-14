class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones.sort()
        j = len(stones) - 1
        i = j-1
        while i >= 0:
            res = stones[j] - stones[i]
            stones = stones[:-2]

            if res == 0:
                i -= 2
                j -= 2
            else:
                fnd = False
                i -= 1
                j -= 1
                for idx in range(j):
                    if res < stones[idx]:
                        fnd = True
                        break
                if fnd:
                    stones = stones[:idx] + [res] + stones[idx:]
                else:
                    stones.append(res)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

if __name__ == "__main__":
    sol = Solution()
    inp = [2,7,4,1,8,1]
    exp = 1
    res = sol.lastStoneWeight(inp)
    print(f'Test 1 - Expected: {exp}, result: {res}')