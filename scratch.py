# Definition for a Node.
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

    def connect(self, root):
        if not root: return root
        lag, node = root, root

        while lag.left:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
                node = node.next
            else:
                lag = lag.left
                node = lag
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