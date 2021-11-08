'''
Key observation is that with 1 value as the root, the left subtree has x values (between 0 and n-1) and the right
subtree has y values, between (n-1 and 0). The total number of ways this binary tree can be construted is num(x)*num(y) summed
over all possible values of x and y.

Did this one by calculating the number of possible binary trees for all numbers less than n and storing.

Apparently this sequence is also known as Catalan numbers and the value can be computed directly. It's a combinatorics problem.
'''

class Solution:
    def numTrees(self, n: int) -> int:
        subtree_vals = {0: 1, 1: 1}

        # Create the number of subtrees for all values 1-n
        for tree in range(2,n+1):
            num_trees = 0
            for i in range(tree):
                l, r = i, tree-1-i
                num_trees += subtree_vals[l]*subtree_vals[r]
            subtree_vals[tree] = num_trees
        return subtree_vals[n]

if __name__ == "__main__":
    sol = Solution()
    n = 19
    print(sol.numTrees(n))