# Complete binary tree: check for first hole (Null value), and make sure no nodes come after it
class Solution:
    def isCompleteTree(self, root) -> bool:
        queue = [root]
        hole = False
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                if hole:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            elif not hole:
                hole = True
        return True