'''
Solving this on 2021/01/05 I had some help from the comments.
Key idea when exploring a search is that at each level look for palindromes by moving the substring end index. 
    >Grow the substring from start to end, don't need to move the start index. These mid strings will get searched in later depths.

There are some nice ways to clean this up. It's probably better to store a string than a set of indices because the string my 
'''
import time
class Solution:
    def is_palindrome(self, s, s_idx, e_idx):
        while s_idx < e_idx:
            if s[s_idx] != s[e_idx]: return False
            s_idx += 1
            e_idx -= 1
        return True

    def partition_o(self, s: str):
        mem = {}
        #e_idx is the ending index, not one past it
        def dfs(s, s_idx, e_idx):
            if (s_idx, e_idx) in mem:
                return mem[(s_idx, e_idx)]
            if s_idx == e_idx:
                return [[s[s_idx]]]
            res = []
            for i in range(s_idx, e_idx+1):
                if self.is_palindrome(s, s_idx, i):
                    pal = s[s_idx:i+1]
                    # If i is at the end we can't slice any more. Add this one on.
                    if i == e_idx:
                        res.append([pal])
                    else:
                        for v in dfs(s, i+1, e_idx):
                            res.append([pal] + v)
            # Store
            mem[(s_idx, e_idx)] = res
            return res
        
        return dfs(s, 0, len(s)-1)
    
    '''
    Solution without using indices in the DFS, so string is stored directly in the mem dict, giving more shared subproblem overlap.
    This solution is quite a bit faster.
    '''
    def partition(self, s: str):
        mem = {}

        def dfs(s):
            if not s: return [[]]

            if s in mem: return mem[s]

            res = []
            for i in range(len(s)):
                # Check for palindrome by reversing string slice
                if s[:i+1] == s[:i+1][::-1]:
                    pal = s[:i+1]
                    for v in dfs(s[i+1:]):
                        res.append([pal] + v)
            # Store
            mem[s] = res
            return res
        
        return dfs(s)

if __name__ == "__main__":
    sol = Solution()
    s = 'aabbaa'

    print(sol.partition(s))
