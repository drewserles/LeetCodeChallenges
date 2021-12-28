'''
Try the trimming approach next.
'''

class Solution:
    def findMinHeightTrees(self, n, edges):
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

        min_height = float('inf')
        label = []
        for i in range(n):
            seen = set([i])
            height = dfs(seen, i)
            if height < min_height:
                min_height = height
                label = [i]
            elif height == min_height:
                label.append(i)
        return label

if __name__ == "__main__":
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    sol = Solution()
    print(sol.findMinHeightTrees(n, edges))