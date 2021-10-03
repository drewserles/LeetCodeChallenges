import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','', s).lower()
        tail = -1
        for i in range(len(s)//2):
            if s[i] != s[tail]:
                return False
            tail -= 1
        return True

if __name__ == "__main__":
    mysol = Solution()
    word = "AbA"
    print(mysol.isPalindrome(word))