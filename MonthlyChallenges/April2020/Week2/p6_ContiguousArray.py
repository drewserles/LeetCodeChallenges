class Solution:
    def findMaxLength(self, nums) -> int:
        hm = {}
        l, max_len, bal = 0, 0, 0
        for n in nums:
            cl = 0
            l += 1
            if n == 1:
                bal += 1
            else:
                bal -= 1
            if bal == 0:
                cl = l
            else:
                if bal in hm:
                    cl = l - hm[bal]
                else:
                    hm[bal] = l
            if cl > max_len:
                max_len = cl
        return max_len


if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0]
    print(sol.findMaxLength(nums))