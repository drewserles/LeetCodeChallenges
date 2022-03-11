class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j=len(num1)-1, len(num2)-1
        carry = 0
        res = ''
        while 1:
            nv = carry
            if i >= 0:
                nv += int(num1[i])
                i -= 1
            if j >= 0:
                nv += int(num2[j])
                j -= 1
            carry = nv // 10
            res += str(nv % 10)
            if i < 0 and j < 0 and carry == 0:
                break
        return res[::-1]

if __name__ == "__main__":
    sol = Solution()
    num1 = "456"
    num2 = "77"
    print(sol.addStrings(num1, num2))