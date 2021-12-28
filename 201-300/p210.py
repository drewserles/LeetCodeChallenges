'''
Idea: create a directed graph from prerequisite course to dependent course.
-A course with no pre-requisite course is a leaf and can be entered in any order
-If there's a cycle in the graph then there's no valid ordering. A cycle is a circular dependency
-Do this as a variant of BFS with a queue.
Key idea is that for a node to be added to the result then its parents (i.e. the courses prerequisites)
need to already be added.
    >Nodes involved in a cycle will never get added to the result because their parents don't get completed. That's good
-Continue while queue has contents. If the child's parents are done then add the child to the queue.
'''
class Solution:
    def findOrder(self, numCourses, prerequisites):
        res = []
        is_req_for = [[] for _ in range(numCourses)]
        depends_on = [[] for _ in range(numCourses)]
        queue = [] # Courses with no re-reqs. Start with these
        
        for prereq in prerequisites:
            c,p = prereq[0], prereq[1]
            is_req_for[p].append(c)
            depends_on[c].append(p)

        done = set()
        for i in range(numCourses):
            if len(depends_on[i]) == 0:
                queue.append(i)

        def finished_parents(node):
            return all(x in done for x in depends_on[node])

        # Start looking at leafs
        while len(queue) > 0:
            node = queue.pop(0)

            # If it's in the queue then it's done. Add it to the results
            done.add(node)
            res.append(node)

            # For each child of this node, if all their parents are done then add them to the queue
            for c in is_req_for[node]:
                # If the child is finished then this is a cycle
                if finished_parents(c):
                    queue.append(c)

        if len(res) < numCourses:
            return []
        else:
            return res
            



if __name__ == '__main__':
    sol = Solution()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(sol.findOrder(numCourses, prerequisites))