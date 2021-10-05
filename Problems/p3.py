'''
Problem 3 (medium): https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        curr, longest = 0, 0
        for i in range(len(s)):
            char = s[i]
            # Haven't seen this character yet
            # OR the last time it was seen is not part of the current substring (occureed before start)
            if (char not in seen) or (seen[char] < i - curr):
                seen[char] = i
                curr += 1
            # Character is part of current substring - change running length to start after previous occurrence
            else:
                if curr > longest:
                    longest = curr
                curr = i - seen[char]
                seen[char] = i
        return max(curr, longest)


if __name__ == "__main__":
    s = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))