'''
'''
class Solution:
    # def findJudge(self, n, trust):
    #     doesnt_trust_anyone = set([x for x in range(1,n+1)])
    #     trusts_them = {}
    #     for x in range(1,n+1):
    #         trusts_them[x] = 0
    #     # The person trusts someone. They're not the judge
    #     for t in trust:
    #         if t[0] in doesnt_trust_anyone:
    #             doesnt_trust_anyone.remove(t[0])
        
    #         trusts_them[t[1]] += 1

    #     for p in doesnt_trust_anyone:
    #         if trusts_them[p] == (n-1):
    #             return p
        
    #     return -1
    
    def findJudge(self, n, trust):
        doesnt_trust_anyone = [1 for _ in range(n+1)]
        trusts_them = [0 for _ in range(n+1)]
        # The person trusts someone. They're not the judge
        for t in trust:
            doesnt_trust_anyone[t[0]] = 0
        
            trusts_them[t[1]] += 1

        for p in range(1, n+1):
            if doesnt_trust_anyone[p] == 1 and trusts_them[p] == (n-1):
                return p
        
        return -1


if __name__ == "__main__":
    sol = Solution()
    n = 1
    trust = []
    print(sol.findJudge(n, trust))