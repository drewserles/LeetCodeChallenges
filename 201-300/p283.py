class Solution:
    def moveZeroes(self, nums) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        return nums
            



if __name__ == '__main__':
    sol = Solution()
    # T1 - Jumble
    inp = [0,1,0,3,12]
    print(sol.moveZeroes(inp))
    # T2 - In order already
    inp = [4, 6, 7, 0, 0]
    print(sol.moveZeroes(inp))
    # T3 - Small cases
    inp = [1]
    print(sol.moveZeroes(inp))
    inp = []
    print(sol.moveZeroes(inp))
    # T4 - No Zero, All Zero
    inp = [10, 4, 9]
    print(sol.moveZeroes(inp))
    inp = [0, 0, 0, 0]
    print(sol.moveZeroes(inp))
    # T5 - Negative values
    inp = [0, -10, 4, 9]
    print(sol.moveZeroes(inp))