'''
    I could make this a lot prettier. Think about what a nice way to do it might be
    -Next steps string ending in 'a' are current strings ending in 'e' + 'i' + 'u'
    e_n = a + i
    i_n = e + o
    o_n = i
    u_n = i + o

    {'a': ['e'],
     'e': ['a', 'i'],
     'i': ['a', 'e', 'o', 'u'],
     'o': ['i', 'u'],
     'u': ['a']}
'''

class Solution:
    def countVowelPermutation(self, n):
        a,e,i,o,u = 0,1,2,3,4
        counts = [1,1,1,1,1]
        for _ in range(1, n):
            a_n = counts[e] + counts[i] + counts[u]
            e_n = counts[a] + counts[i]
            i_n = counts[e] + counts[o]
            o_n = counts[i]
            u_n = counts[i] + counts[o]
            counts = [a_n, e_n, i_n, o_n, u_n]
        return sum(counts) % (10**9 + 7)

if __name__ == "__main__":
    sol = Solution()
    print(sol.countVowelPermutation(5))

# Bonus DFS version. Much slower, but a good lesson
# class Solution:
#     def __init__(self):
#         self.next_char = {'a': ['e'],
#                 'e': ['a', 'i'],
#                 'i': ['a', 'e', 'o', 'u'],
#                 'o': ['i', 'u'],
#                 'u': ['a']}

#     def dfs(self, last_char, targ_len, cur_len):
#         if targ_len == cur_len:
#             return 1
#         next_chars = self.next_char[last_char]
#         found = 0
#         for c in next_chars:
#             found += self.dfs(c, targ_len, cur_len+1)
#         return found

#     def countVowelPermutation(self, n):
#         valid = 0
#         for c in ['a', 'e', 'i', 'o', 'u']:
#             valid += self.dfs(c, n, 1)
#         return valid % (10**9 + 7)