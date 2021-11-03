class Solution:
    def groupAnagrams(self, strs):
        # How to keep trackof contents but order doesn't matter? Could sort them
        # Dictionary where the key is the sorted key, the values are a list of words?
        res = {}
        for s in strs:
            # Did not know this originally: sorted() creates a list from strings - no need to call list on it first
            char_key = ''.join(sorted(s))
            if char_key not in res:
                res[char_key] = [s]
            else:
                res[char_key].append(s)
        return res.values()


if __name__ == '__main__':
    sol = Solution()
    # T1 - Provided example
    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # inp = ["eat", "ate"]
    exp = [["ate","eat","tea"], ["nat","tan"], ["bat"]]
    res = sol.groupAnagrams(inp)
    print(f'Test 1 - Expected: {exp}, result: {res}')

    # T2 - Tricky
    inp = ["att", "aat", "aatt", "tat"]
    exp = [["att", "tat"], ["aat"], ["aatt"]]
    res = sol.groupAnagrams(inp)
    print(f'Test 2 - Expected: {exp}, result: {res}')