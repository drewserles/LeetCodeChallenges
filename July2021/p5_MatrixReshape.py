class Solution:
    def matrixReshape(self, mat, r, c):
        r_o, c_o = len(mat), len(mat[0])
        if r_o*c_o != r*c:
            return mat
        
        res = [[0 for col in range(c)] for row in range(r)]
        i_o, j_o = 0,0
        for i in range(r):
            for j in range(c):
                res[i][j] = mat[i_o][j_o]
                j_o += 1
                if j_o >= c_o:
                    j_o = 0
                    i_o += 1
        return res


sol = Solution()
mat = [[1,2],[3,4]]
r = 1
c = 4
print(sol.matrixReshape(mat, r, c))

        
