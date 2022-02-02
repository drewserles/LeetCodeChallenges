'''
Idea: keep a dictionary of the letter count in p then also maintain a running tally of the characters in the current slice of s.
Step through s one character at a time, dropping the previous character off the count and adding the next character

Speed up idea 1: don't need to maintain the current dictionary with letters that aren't in the anagram. You'll see that it's not an anagram
because the letter count won't match for the anagram letters

Speed up idea 2: If a letter at idx i isn't in p then that section is never going to be an anagram until idx i is dropped off.
    Could jump to i+1, recreate the dictionary slice, and continue

^Nice, that one takes it from 56th% to 99.4%th
'''

class Solution:
    def findAnagrams(self, s: str, p: str):
        def create_slice_dict(inp_str, inp_dict):
            dict = {}
            for k in inp_dict.keys():
                dict[k] = 0
            for c in inp_str:
                if c in dict:
                    dict[c] += 1
            return dict
        
        # Construct a dictionary of the anagram for letter counts
        gram_dict = {}
        for c in p:
            if c not in gram_dict:
                gram_dict[c] = 1
            else:
                gram_dict[c] += 1
        
        # Setup
        res = []
        L = len(p)
        cur_dict = create_slice_dict(s[:L], gram_dict)
        i = 0

        while True:
            # print(i, cur_dict, gram_dict)
            # Check and add
            if cur_dict == gram_dict:
                res.append(i)
            
            # Increment and get the next one
            i += 1
            if i > (len(s) - L):
                break

            old_l = s[i-1]
            new_l = s[i + L - 1]

            if old_l in cur_dict:
                cur_dict[old_l] -= 1

            # New letter isn't part of the anagram -> skip to after it
            if new_l not in cur_dict:
                i += L
                cur_dict = create_slice_dict(s[i:i+L], gram_dict)

            else:
                cur_dict[new_l] += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    s = "bbaa"
    p = "aa"
    print(sol.findAnagrams(s, p))