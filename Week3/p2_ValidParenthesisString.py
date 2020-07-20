class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            # ')'
            else:
                if len(left) > 0:
                    left.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
        while len(left) > 0:
            l = left.pop()
            loc = -1
            if len(star) > 0:
                loc = star.pop()
            if l > loc:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    inp = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
    print(sol.checkValidString(inp))