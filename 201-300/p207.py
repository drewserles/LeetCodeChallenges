'''
Less complicated version of 210. Just returning true if a cycle isn't found.
Let's do it a different way
'''
class Solution:
    
    def findOrder(self, numCourses, prerequisites):
        seen = [0 for _ in range(numCourses)]
        dependents = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            c,p = prereq[0], prereq[1]
            dependents[p].append(c)

        def dfs(node):
            seen[node] = 1
            for c in dependents[node]:
                if seen[c] == 0:
                    if not dfs(c):
                        return False
                elif seen[c] == 1:
                    return False
            seen[node] = 2
            return True

        for n in range(numCourses):
            if seen[n] == 0:
                if not dfs(n):
                    return False

        return True

if __name__ == '__main__':
    sol = Solution()
    numCourses = 20
    prerequisites = [[1,0], [2,1], [0,2]]
    print(sol.findOrder(numCourses, prerequisites))