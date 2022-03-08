class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        i=1
        cnt=1
        max_cnt = 0
        while i < len(nums):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
            i += 1
        return max(max_cnt, cnt)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,4,7]
    print(sol.findLengthOfLCIS(nums))