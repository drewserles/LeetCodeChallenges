class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # First letter is lowercase - rest of word must be lower
        if word[0] == word[0].lower():
            return word[1:] == word[1:].lower()
        # First letter capital - rest of word is lowercase or uppercase
        else:
            return word[1:] == word[1:].lower() or word[1:] == word[1:].upper()



if __name__ == "__main__":
    sol = Solution()
    word = "usaA"
    print(sol.detectCapitalUse(word))