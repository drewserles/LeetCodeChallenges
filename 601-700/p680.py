'''
Allow one character deletion. This means you can skip one character
Strategy:
Do a normal palindrome detection, if it's a palindrome return True.
If you get to an issue try skipping a letter in either direction and explore both those branches. If either one returns True return that
'''

class Solution:
    def validPalindrome(self, s):
        def pal_func(s, i, j, deleted):
            while i < j:
                if s[i] != s[j]:
                    if deleted:
                        return False
                    else:
                        return pal_func(s, i+1, j, True) or pal_func(s, i, j-1, True)
                else:
                    i += 1
                    j -= 1
            return True
        
        
        return pal_func(s, 0, len(s)-1, False)


if __name__ == "__main__":
    sol = Solution()
    s = "abb"
    print(sol.validPalindrome(s))