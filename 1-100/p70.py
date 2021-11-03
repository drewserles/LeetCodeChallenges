'''
Problem 70 (easy): https://leetcode.com/problems/climbing-stairs/

Key: the number of ways to get to a step is # of ways to previous step + # of ways to two steps ago
Just need to track the two values. Fibonacci sequence
'''

class Solution:
    def climbStairs(self, n):
        p1, p2 = 1, 1
        for _ in range(1, n):
            p1, p2 = p1 + p2, p1
        return p1


if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.climbStairs(n))