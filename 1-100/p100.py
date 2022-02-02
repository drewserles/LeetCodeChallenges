# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Idea: do a traversal of the two trees and check if the traversals are equal.
>Traverse the tree with value first then children, otherwise it doesn't work. Tried in order traversal and it failed
>Need a placeholder for an empty child node, e.g. None, otherwise different trees could have the same traversal
'''
class Solution:
    def isSameTree_dfs(self, p, q) -> bool:
        def traversal(root):
            if not root:
                return [None]
            else:
                return [root.val] + traversal(root.left) + traversal(root.right)
        
        return traversal(p) == traversal(q)

    # Alternatively could do it with BFS -> check each level before going on to the next
    def isSameTree(self, p, q) -> bool:
        def check_nodes(p, q):
            if not p and not q:
                return True
            elif not q or not p or (p.val != q.val):
                return False
            else:
                return True
        
        nodes, i = [(p,q)], 0
        while i < len(nodes):
            p,q = nodes[i][0], nodes[i][1]
            if not check_nodes(p, q):
                return False
            elif p and q:
                nodes.append((p.left, q.left))
                nodes.append((p.right, q.right))
            i += 1
        return True

if __name__ == "__main__":
    sol = Solution()
    
    p4 = TreeNode(1)
    p3 = TreeNode(3)
    p2 = TreeNode(2, left=p4)
    p1 = TreeNode(1, left=p2, right=p3)

    q4 = TreeNode(1)
    q3 = TreeNode(3)
    q2 = TreeNode(2, left=q4)
    q1 = TreeNode(1, left=q2, right=q3)


    print(sol.isSameTree(p1, q1))