import math

class Solution:
    # iterative solution
    def arrangeCoins(self, n: int) -> int:
        coins, row = 0, 0
        while coins <= n:
            row += 1
            coins += row
        return row-1

    '''
    Direct solution taking advantage of sum = n*(n+1)/2
    sum is the input number n, n is the row number. re-arrange to 2n = r^2 + r, 0 = r^2 + r - 2n
    Can solve this with quadratic formula and then take the floor (non decimal) of the answer to represent the completed rows
    Note since 2n = c is always positive we only need the + portion of the quadratic.
    
    => could also complete the square and get an equation for k.
    '''
    def arrangeCoins2(self, n: int) -> int:
        return int((-1 + (1 + 8*n)**(1/2))/2)

if __name__ == "__main__":
    sol = Solution()
    n = 8
    print(sol.arrangeCoins2(n))