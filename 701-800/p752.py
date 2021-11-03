'''
>Dial with 10 numbers, can be rotate forward (0 -> 9) or backwards (9 -> 0)

>Treat it as a finding shortest path problem - from 0000 to your target password
>Each combination can be represented as a node on a graph. 10,000 nodes from 0000 to 9999
>The number of connections is not actually that bad because it's only from one valid combination to the next valid combination
e.g. 1034 had an edge to 1035 and 1023 but not 1036. 8 connections for each node actually. Just up and down for each number
>Then remove out edges from the dead ends. If we get to them then you can't go anywhere else

From there we can use a shortest path algorithm. I'm going to use BFS because I used it recently in my course.
'''

class Solution:
    def __init__(self):
        # Given a dial number, what numbers can be reached. Easy hardcode
        self.rotations = {'0': ['1', '9'], '1': ['2', '0'], '2': ['3', '1'],
                '3': ['4', '2'], '4': ['5', '3'], '5': ['6', '4'],
                '6': ['7', '5'], '7': ['8', '6'], '8': ['9', '7'], '9': ['0', '8']}

    def valid_next_codes(self, num):
        codes = []
        for i in range(4):
            b = num[:i]
            valid = self.rotations[num[i]]
            a = num[i+1:]
            codes += [b + valid[0] + a, b + valid[1] + a]
        return codes

    def openLock(self, deadends, target):
        deadends = set(deadends)
        seen = {}
        queue = []
        lock_start = '0000'
        if lock_start not in deadends:
            seen[lock_start] = 0
            queue.append(lock_start)
        
        # Loop until queue is empty (failure) or path found
        while len(queue) > 0:
            node = queue.pop(0)
            dist = seen[node]
            
            # Found the target, return number of moved required to get there (distance from origin)
            if node == target:
                return dist
            
            next_steps = self.valid_next_codes(node)
            
            # Enqueue all the valid nodes that this one touches
            for next in next_steps:
                if next not in seen and next not in deadends:
                    seen[next] = dist + 1
                    queue.append(next)

        # Return -1 for no path
        return -1



if __name__ == "__main__":
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = '8888'
    sol = Solution()

    print(sol.openLock(deadends, target))