'''
My first observation is the column names are a numbering system in base 26, rather than base 2 or base 10.
A is your 0, Z is your 25 (analogous to 1 or 9) and the next value rolls you over.
Make a system that parses this.
-Need a function to convert to single character to number. Instead of creating a big dictionary I'll just use the ascii code. 'A' is 65, so can subtract 64 off everything
    to get A-Z in range 1-26
-Process a title by iterating left to right and keep track of a running total. For each character, multiply your total by 26 (left shift in base 26) and add the new character value.
'''

class Solution:
    
    def titleToNumber(self, columnTitle):
        def char_to_num(char):
            return ord(char)-64
        tot = 0
        for c in columnTitle:
            tot *= 26
            tot += char_to_num(c)
        return tot


if __name__ == "__main__":
    sol = Solution()
    columnTitle = "AAA"
    print(sol.titleToNumber(columnTitle))