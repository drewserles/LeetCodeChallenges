'''
Ideas
-No swap needed when a number's digits are in descending order
-The best swap is the one that gets the biggest number possible into a leftmost position. Formalize this

Brute force
-step from left to right through the digits
-Each time look for a bigger number in every digit after it. If you find one swap them and stop
-Realized the second pointer should move up from the end of the array in the event of a tie for best candidate
-This could be an O(n^2) solution in the worst case. Is there a better way?

Better
Move right to left through the array. At each entry, store the max value seen so far and its index
Then move left to right. Check if the max store value is greater than this value. If it is then swap them and exit
'''

class Solution:
    def maximumSwap_v1(self, num):
        num=[d for d in str(num)]
        for i in range(len(num)-1):
            max_val = num[i]
            max_idx = -1
            for j in reversed(range(i+1, len(num))):
                if num[j] > max_val:
                    max_val = num[j]
                    max_idx = j
            if max_idx != -1:
                num[i],num[max_idx] = num[max_idx],num[i]
                break
        return int(''.join(num))

    def maximumSwap(self, num):
        num=[d for d in str(num)]
        max_seen = [None for _ in range(len(num))]
        
        max_val_idx = -1
        max_val = '0'
        for j in reversed(range(len(num))):
            if num[j] > max_val:
                max_val = num[j]
                max_val_idx = j
            max_seen[j] = (max_val, max_val_idx)
        
        for i in range(len(num)-1):
            if max_seen[i][0] > num[i]:
                swap_idx = max_seen[i][1]
                num[i], num[swap_idx] = num[swap_idx], num[i]
                break
        return int(''.join(num))



if __name__ == "__main__":
    sol = Solution()
    num = 1909
    print(sol.maximumSwap(num))