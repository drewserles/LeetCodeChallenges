'''
Try the trimming approach next.
'''

class Solution:
    def findMinHeightTrees_dfs(self, n, edges):
        comps = [[] for _ in range(n)]
        for e in edges:
            comps[e[0]].append(e[1])
            comps[e[1]].append(e[0])

        cache = {}

        def dfs(seen, node):
            max_depth = 0

            for n in comps[node]:
                if n not in seen:
                    seen.add(n)
                    # Check if this combination of parent child is in the cache already
                    if (node, n) in cache:
                        dfh = cache[(node,n)]
                    else:
                        dfh = dfs(seen, n)
                        cache[(node,n)] = dfh
                    max_depth = max(max_depth, dfh)
            return 1 + max_depth

    '''
    DFS approach is O(N^2) in its worst case (even with the nice cache)
    There's an approach relating to sorting and trimming that's O(n). I had some help on this one
    with the general strategy. Implementing here to learn
    '''
    def findMinHeightTrees(self, n, edges):
        if n <= 2: return [i for i in range(n)]
        
        # Construct the adjacency list
        adj = [[] for _ in range(n)]
        in_count = [0 for _ in range(n)]
        rem_nodes = n

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
            in_count[e[0]] += 1
            in_count[e[1]] += 1

        # Iteratively trim off the nodes with 1 in edge and remove them from the adjacency list
        # How does it end? I need to know when I'm down to the last node/nodes. I could keep track of the max in some way,
        # Or if the number removed is equal to all that remain then it's done

        # How do I cleverly track the 1 in edges?
        # I could build a list during the adjacency list, then when I pop those off each time I could check if
        ones = set([i for i in range(n) if len(adj[i]) == 1])

        while 1:
            if len(ones) == rem_nodes:
                return list(ones)

            # Trim the one edge nodes
            new_ones = set()
            
            for n in ones:
                # Trim it
                in_count[n] -= 1
                rem_nodes -= 1
                # all nodes connected to this one
                rem = adj[n]
                # Iterate through them and decrement. If it's 1 add it to the next 1s
                for v in rem:
                    in_count[v] -= 1
                    if in_count[v] == 1:
                        new_ones.add(v)
            ones = new_ones

if __name__ == "__main__":
    # n = 3
    # edges = [[0,1], [1,2]]
    n = 2
    edges = [[0,1]]
    sol = Solution()
    print(sol.findMinHeightTrees(n, edges))