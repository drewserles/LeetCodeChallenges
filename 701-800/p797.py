'''
Nov 2021 BFS solution. Need to keep track of the paths seen so far because the answer is a list paths, but
do not need to track nodes seen before. Since it's acyclic you'll never get caught in a loop, so any path to a node
is a valid one to explore. E.g. A->B->C is valid and different from D->B->C even though it follows the same path through B to end node C.

Looks like I submitted a solution to this over 3 years ago, which would have been Insight prep time.
I think that solution is a bit incorrect since it looks for the empty [] on the final node. But you could have graphs that have
nodes leading nowhere but are not the final node, so that solution should fail with good test cases. I guess it snuck by.
'''

class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph) # Num nodes, 0 to n-1
        queue = [[0]] # Paths to explore. Search from the most recent node (idx -1)
        results = []
        while len(queue) > 0:
            path = queue.pop(0)
            current_node = path[-1]
            reachable = graph[current_node] # reachable nodes from here. This is a list
            for node in reachable:
                new_path = path + [node]
                if node == n-1:
                    results.append(new_path)
                else:
                    queue.append(new_path)
        return results

if __name__ == "__main__":
    sol = Solution()
    graph = [[1,3],[2],[3],[]]
    print(sol.allPathsSourceTarget(graph))