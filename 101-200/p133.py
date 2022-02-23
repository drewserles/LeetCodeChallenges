'''
Specifications from the problem:
-Test case is an adjacency list, but the function get called with a Node as input. 
-Input node is always value 1, graph is connected so every node is reachable from 1. 
-Return a clone of node 1 that properly connects to a clone of the rest of the graph.

Strategy to do this:
-Start with the inp node in the queue
-Keep a dictionary mapping from existing node to new version of that node
-While the queue exists:
    -pop off the first node (this is old version)
    -Look through its neighbors. if they're not in the node dictionary, create the new version and add it
    -Add the new version of all neighbor nodes to a list
    -If the neighbor nodes have not already been explored add them to the queue
    -Add the list of new version of neighbor nodes to the new version of current node
    -Mark current node (old version) as visited
'''

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        node_dict = {}
        visited = set()
        node_dict[node] =  Node(node.val)
        queue = [node]

        while len(queue) > 0:
            cn = queue.pop(0)
            neighbors = []
            # Look through its neighbours. 
            for n in cn.neighbors:
                # If not in the node dict then create it
                if n not in node_dict:
                    # new_node = Node(n.val)
                    node_dict[n] = Node(n.val)
                # Add the new node to the neighbours list
                neighbors.append( node_dict[n] )
                # If the (old version) node hasn't already been visited then add it to the queue
                if n not in visited:
                    queue.append(n)
            # Add the neighbor list to the new node
            node_dict[cn].neighbors = neighbors
            # Add this node (old version) to visited
            visited.add(cn)

        return node_dict[node]


if __name__ == "__main__":
    sol = Solution()
    # Test case format
    inp_adj = [[2,4],[1,3],[2,4],[1,3]]

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2,n4]
    n2.neighbors = [n1,n3]
    n3.neighbors = [n2,n4]
    n4.neighbors = [n1,n3]

    # Always call the function with the value 1 node
    new_head = sol.cloneGraph(n1)
    print(new_head.neighbors[0].val, new_head.neighbors[1].val)