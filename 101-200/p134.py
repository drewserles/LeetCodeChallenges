'''
Idea: if we can take a forward step do it. If not (because tank is empty) then we would need more gas
from earlier in the circuit, so move the starting location back by one.
'''
class Solution:
    def canCompleteCircuit(self, gas, cost):
        stops = len(gas)
        
        start,cur, tot = 0,0, 0
        
        while 1:
            # Currently gas tank is positive. Trying going forward
            if tot >= 0:
                tot += (gas[cur] - cost[cur])
                cur = (cur + 1) % stops
            # Otherwise try moving the start back
            else:
                start = (start-1) % stops
                tot += (gas[start] - cost[start])
            if cur == start:
                break
        if tot >= 0:
            return start
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    gas = [1,2]
    cost = [2,1]
    print(sol.canCompleteCircuit(gas, cost))