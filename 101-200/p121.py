class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        min_val = float('inf')
        for p in prices:
            if p - min_val > profit:
                profit = p - min_val
            if p < min_val:
                min_val = p
        return profit


if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))