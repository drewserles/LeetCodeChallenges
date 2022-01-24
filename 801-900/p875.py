'''
Binary search problem

Algorithm: choose a banana eating speed and calculate the number of hours it would take to eat them all at that speed
IF the hours is <= h (guard hours) this is a valid answer. Record it if it's lower then existing
    then try a lower eating speed -> this will increase hours
IF the hours is > h then we're not eating fast enough. Try a bigger speed
Do this with binary search - split the difference and iterate
'''

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        if len(piles) > h: return False
        # k is banana eating speed
        min_k = 1
        max_k = max(piles) # The biggest would be eating the biggest pile in one hour
        lowest_k = max_k
        
        while min_k <= max_k:
            k = (min_k + max_k) // 2
            eat_time = sum((p // k + (1 if p%k > 0 else 0)) for p in piles)
            if eat_time <= h:
                if k < lowest_k:
                    lowest_k = k
                max_k = k-1 #adjust range
            else:
                min_k = k+1
        return lowest_k


if __name__ == "__main__":
    sol = Solution()
    piles = [30]
    h = 5
    print(sol.minEatingSpeed(piles, h))