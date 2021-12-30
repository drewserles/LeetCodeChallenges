class Solution:
    def kClosest(self, points, k):
        dist = {}
        for p in points:
            d = p[0]**2 + p[1]**2
            if d in dist:
                dist[d].append(p)
            else:
                dist[d] = [p]
        res = []
        for key in sorted(dist.keys()):
            for pair in dist[key]:
                if len(res) >= k:
                    return res
                res.append(pair)
        return res

    # Ultra pythonic way
    def kClosest_2(self, points, k):
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]

if __name__ == "__main__":
    sol = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(sol.kClosest(points, k))
    print(sol.kClosest_2(points, k))