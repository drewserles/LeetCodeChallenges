'''
This works but it's too slow
'''
class Solution:
    def largestComponentSize(self, nums):
        def sieve(num):
            factors = set()
            i = 2
            while i*i <= num:
                if num % i == 0:
                    num /= i
                    factors.add(i)
                else:
                    if i == 2:
                        i += 1
                    else:
                        i += 2
            if num > 1:
                factors.add(int(num))
            return factors
        
        # Get prime factorization for each number
        factors = [sieve(n) for n in nums]
        
        # Build a graph: connection between numbers based on factorization
        # Compare every value to every other value in construction (n^2)
        graph = {n:[] for n in nums}
        for i1 in range(len(nums)-1):
            for i2 in range(i1+1, len(nums)):
                if len(factors[i1].intersection(factors[i2])) > 0:
                    v1,v2 = nums[i1], nums[i2]
                    graph[v1].append(v2)
                    graph[v2].append(v1)
        
        # DFS on graph to find largest number of components
        seen = set()
        def dfs(n):
            if n in seen:
                return 0
            else:
                seen.add(n)
                return 1 + sum([dfs(n_c) for n_c in graph[n]])

        max_sz = 0
        for n in nums:
            sz = dfs(n)
            if sz > max_sz:
                max_sz = sz
        return max_sz





if __name__ == "__main__":
    sol = Solution()
    nums = []
    print(sol.largestComponentSize(nums))