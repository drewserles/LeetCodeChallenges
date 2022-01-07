'''
The final one runs fast enough.
'''

class Solution:
    def palindromeLength(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-(1+i)]:
                return False
        return True
    

    def longestPalindrome_v0(self, s: str) -> str:
        max_str = s[0]
        pairs = []
        # Index the string
        char_idx = {}
        for i in range(len(s)):
            if s[i] not in char_idx:
                char_idx[s[i]] = [i]
            else:
                char_idx[s[i]].append(i)


        for v in char_idx.values():
            for i in range(len(v)):
                for j in range(i+1, len(v)):
                    start_idx,end_idx = v[i],v[j]+1
                    pairs.append((start_idx, end_idx, end_idx - start_idx))
        pairs.sort(key=lambda x: x[2], reverse=True)
        
        for p in pairs:
            start_idx,end_idx = p[0], p[1]
            sub_str = s[start_idx:end_idx]
            if self.palindromeLength(sub_str):
                return sub_str
        
        return max_str

    # What about just bruteforcing it with a bit of early exit (ie considering the longest ones first)
    def longestPalindrome_v1(self, s: str) -> str:
        str_len = len(s)
        for sub_len in range(len(s), 0, -1):
            for start_idx in range(0, str_len-sub_len+1):
                sub_str = s[start_idx: start_idx+sub_len]
                if sub_str == sub_str[::-1]:
                    return sub_str

    # Can I work smallest to largest and save what I've found? Could use that to lower the number of palindrome checks
    def longestPalindrome_v2(self, s:str):
        longest, max_len, mem = s[0], 1, set()

        for pal_len in range(2, len(s)+1):
            for start_idx in range(0, len(s) - pal_len + 1):
                end_idx = start_idx+pal_len-1
                # check if first and last letters match and centre is a palindrome
                if s[start_idx] == s[end_idx] and ((pal_len < 4) or (s[start_idx+1:end_idx] in mem)):
                    # then: this is valid. update longest, add it to memory
                    mem.add(s[start_idx:end_idx+1])
                    if pal_len > max_len:
                        max_len = pal_len
                        longest = s[start_idx:end_idx+1]
        return longest

    # Middle out check
    def longestPalindrome(self, s):
        self.longest = s[0]

        def search(l, r):
            # I like these and conditions - it will either end by going out of bound or when it doesn't match. And when it does you know the previous look was valid
            # Fairly nice catch all for even/odd length palindromes and no palindrome strings
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(self.longest):
                self.longest = s[l+1:r]

        for i in range(len(s)):
            # Even length palindromes with double middle
            search(i, i+1)
            # Odd palindrome with single middle
            search(i-1, i+1)

        return self.longest
                





if __name__ == "__main__":
    s = "abcba"
    sol = Solution()
    print(sol.longestPalindrome(s))


# Failing on massive input. E.g.
# "twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# Need new strategy?