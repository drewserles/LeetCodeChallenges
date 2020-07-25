class Solution:
    def maxProfit(self, prices) -> int:
        # Key: Since you can buy and sell whenever, you can capture all swings of the price.
        # So any price increase is profit
        tp = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                tp += (prices[i] - prices[i-1])
        return tp


if __name__ == '__main__':
    sol = Solution()
    # T1 - Base
    inp = [7,1,5,3,6,4]
    exp = 7
    res = sol.maxProfit(inp)
    print(f'Test 1 - Expected: {exp}, result: {res}')
    # T2 - All ascneding
    inp = [1,2,3,4,5]
    exp = 4
    res = sol.maxProfit(inp)
    print(f'Test 2 - Expected: {exp}, result: {res}')
    # T3 - All descending
    inp = [7,6,4,3,1]
    exp = 0
    res = sol.maxProfit(inp)
    print(f'Test 3 - Expected: {exp}, result: {res}')
    # T4 - Small arrays
    inp = [7]
    exp = 0
    res = sol.maxProfit(inp)
    print(f'Test 4 - Expected: {exp}, result: {res}')