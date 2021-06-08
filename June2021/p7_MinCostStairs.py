'''
Key to notice is all the information that needs to be retained is the minimum cost to get to the previous two stairs.
Then since you can jump 1 or 2 stairs, the cost to get to the current stair is the lesser of total cost coming from
previous stair (min cost to get to that stair plus its own cost) and coming from 2 back.
'''
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        to_p1_cost, to_p2_cost = 0,0
        num_stairs = len(cost)
        i = 2
        while i <= num_stairs:
            min_here = min(to_p1_cost + cost[i-1], to_p2_cost + cost[i-2])
            to_p2_cost = to_p1_cost
            to_p1_cost = min_here
            i += 1
        return to_p1_cost

if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    sol = Solution()
    assert(sol.minCostClimbingStairs(cost) == 6)