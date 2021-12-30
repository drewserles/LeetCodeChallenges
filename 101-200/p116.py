class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def print_order(self, root):
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            valu = None
            if node.next:
                valu = node.next.val
            print(f'Val: {node.val}, next: {valu}')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Works but uses memory to store nodes at that level
    def connect_bfs(self, root):
        level_nodes = [root]
        while 1:
            if not level_nodes[0]:
                break
            # First set the next node for this level
            for n in range(len(level_nodes)-1):
                level_nodes[n].next = level_nodes[n+1]
            # Then create the next level
            level_nodes = [x for n in level_nodes for x in (n.left, n.right)]
        return root

    # Can I create a solution that only uses constant extra memory?
    # BFS with constant mem - taking advantage of the next pointer to traverse
    def connect_bfs_mem(self, root):
        #
        link, trav = root, root

        while link:
            # Traverse this depth layer
            while trav and trav.left:
                # link up children
                trav.left.next = trav.right
                # if a next node exists, link up current node's right child to next node's left child
                if trav.next:
                    trav.right.next = trav.next.left
                # Next node on this layers
                trav = trav.next
            # Go to the next depth row - on the left node
            link = link.left
            trav = link
        return root

    # DFS approach - recursive calls
    def connect(self, root):
        if root and root.left:
            root.left.next = root.right
            # if a next node exists, link up current node's right child to next node's left child
            if root.next:
                root.right.next = root.next.left

            _ = self.connect(root.left)
            _ = self.connect(root.right)
        return root

if __name__ == "__main__":
    l7 = Node(7)
    l6 = Node(6)
    l5 = Node(5)
    l4 = Node(4)
    l3 = Node(3, l6, l7)
    l2 = Node(2, l4, l5)
    l1 = Node(1, l2, l3)

    sol = Solution()
    sol.print_order(l1)
    print('- - -')

    sol.connect(l1)

    sol.print_order(l1)
