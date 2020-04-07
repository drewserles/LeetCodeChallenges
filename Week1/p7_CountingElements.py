class Solution:
    def countElements(self, arr) -> int:
        # Count elements x such that x+1 is also in arr
        # Duplicates are counted seperately
        
        # Start with the first point. Don't worry about duplicates
        seen = {}
        cnt = 0
        # X
        for n in arr:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        for k in seen.keys():
            if k+1 in seen:
                cnt += seen[k]
        return cnt



if __name__ == '__main__':
    sol = Solution()
    # T1 - Provided example
    inp = [1, 2, 3]
    exp = 2
    res = sol.countElements(inp)
    print(f'Test 1 - Expected: {exp}, result: {res}')
    # T2 - Provided example
    inp = [1,1,3,3,5,5,7,7]
    exp = 0
    res = sol.countElements(inp)
    print(f'Test 2 - Expected: {exp}, result: {res}')
    # Extras
    inp = [1, 1, 2]
    exp = 2
    res = sol.countElements(inp)
    print(f'Test E - Expected: {exp}, result: {res}')