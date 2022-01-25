class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # First letter is lowercase - rest of word must be lower
        if word[0] == word[0].lower():
            return word[1:] == word[1:].lower()
        # First letter capital - rest of word is lowercase or uppercase
        else:
            return word[1:] == word[1:].lower() or word[1:] == word[1:].upper()

    # I also liked this state based approach I made
    # def detectCapitalUse(self, word: str) -> bool:
    #     s = 0
        
    #     for c in word:
    #         v = ord(c)
    #         # Init state
    #         if s == 0:
    #             if v >= 97:
    #                 s = 1
    #             else:
    #                 s = 2
    #         # ca

    #         # all lower
    #         elif s == 1:
    #             if v < 97:
    #                 return False
    #         # Cap undecided
    #         elif s == 2:
    #             if v >= 97:
    #                 s = 4
    #             else:
    #                 s = 3

    #         # all cap
    #         elif s == 3:
    #             if v >= 97:
    #                 return False

    #         #cap-lower
    #         elif s == 4:
    #             if v < 97:
    #                 return False
    #     return True



if __name__ == "__main__":
    sol = Solution()
    word = "usaA"
    print(sol.detectCapitalUse(word))