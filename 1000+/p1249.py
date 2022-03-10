'''
Strategy:
-Walk through s and keep track of the parentheses we come across L:'(', R:')'
-Rules are: if you come across a L bracket, store it. If you come across a R brack it try to remove a L bracket, if there isn't one store the right
    Once stored a right can never come off
-At the end, whatever's left over needs to be deleted

Could speed it up a tiny bit by storing the letters in a list and just deleting them by setting their value to ''. Note a bracket never comes off
r_brack once it goes on so you could delete right there.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l_brack = []
        r_brack = []
        for i in range(len(s)):
            if s[i] == '(':
                l_brack.append(i)
            elif s[i] == ')':
                if len(l_brack) > 0:
                    _ = l_brack.pop()
                else:
                    r_brack.append(i)
        res = ''
        bracks = set(l_brack).union(set(r_brack))
        for i in range(len(s)):
            if i not in bracks:
                res += s[i]
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "a)b(c)d"
    print(sol.minRemoveToMakeValid(s))