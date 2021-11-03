'''
Problem 1143 (medium): https://leetcode.com/problems/longest-common-subsequence/
'''

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        rows, cols = len(text1), len(text2)
        matrix = [[0 for col in range(cols)] for row in range(rows)]
        
        # The rest
        for i in range(rows):
            for j in range(cols):
                if text1[i] == text2[j]:
                    if i >= 1 and j >= 1:
                        matrix[i][j] = matrix[i-1][j-1]+1
                    else:
                        matrix[i][j] = 1
                else:
                    if i == 0:
                        pr = 0
                    else:
                        pr = matrix[i-1][j]
                    if j == 0:
                        pc = 0
                    else:
                        pc = matrix[i][j-1]

                    matrix[i][j] = max(pr, pc)
        return matrix[-1][-1]


if __name__ == "__main__":
    text1 = "abcba"
    text2 = "abcbcba"
    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))