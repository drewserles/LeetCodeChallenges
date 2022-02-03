'''
4sum
Strategy: do what I did in 3sum (p15) extended to 4. Outside index walks the array, then try to build tripplets for the matching deficit
'''
class Solution:
    # Modify from p15 to take in a target value and a starting index so I don't need to slice the array each time
    def threeSum(self, nums, start_idx, target_val):
        res = []

        for fi in range(start_idx, len(nums) - 2):
            # If this number's the same as the previous index then skip since we want unique values
            if fi > start_idx and nums[fi] == nums[fi-1]:
                continue

            # 2 more pointers - one starting just after fi, one at the end of the array
            si, ti = fi+1, len(nums)-1
            while si < ti:
                sum_val = nums[fi] + nums[si] + nums[ti]
                if sum_val > target_val or ( ti < len(nums)-1 and nums[ti] == nums[ti+1]):
                    ti -= 1
                # too small then move up second index
                elif sum_val < target_val:
                    si += 1
                # Match
                else:
                    res.append([nums[fi], nums[si], nums[ti]])
                    si += 1
                    ti -= 1
        return res

    def fourSum(self, nums, target):
        nums.sort()
        res = []

        for i in range(len(nums)-3):
            # Skip if it's the same value as previous index - to prevent duplicate results
            if i > 0 and nums[i] == nums[i-1]:
                continue

            balance = target - nums[i]
            triples = self.threeSum(nums, i+1, balance)
            for trip in triples:
                res.append([nums[i]] + trip)
        return res



if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(sol.fourSum(nums, target))
    
    
