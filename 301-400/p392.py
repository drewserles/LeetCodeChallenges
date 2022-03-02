class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while 1:
            if i == len(s):
                return True
            if j == len(t):
                return False
            if s[i] == t[j]:
                i += 1
            j += 1

if __name__ == "__main__":
    sol = Solution()
    s = "s"
    t = ""
    print(sol.isSubsequence(s,t))