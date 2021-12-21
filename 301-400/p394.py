
class Solution:
    def extract(self, s, idx):
        '''
        4 Rules.
        -If it's a regular character add it to the working string
        -If it's a number, construct the multiplier until an open bracket is found
        -If it's an open bracket go a level deeper
        -If it's a closing bracket return
        '''
        res, mult = '', 0
        while idx < len(s):
            c = s[idx]
            # Found a number, keep track of it as a multiplier
            if 48 <= ord(c) and ord(c) <= 57:
                mult *= 10
                mult += int(c)
            elif c == '[':
                brack_str, idx = self.extract(s, idx+1)
                res += mult*brack_str
                mult = 0
            elif c == ']':
                return res, idx
            # letter
            else:
                res += c

            idx += 1
        return res

    def decodeString(self, s):
        return self.extract(s, 0)
                





if __name__ == "__main__":
    sol = Solution()
    s = "2[a2[b2[c]]]"
    print(sol.decodeString(s))