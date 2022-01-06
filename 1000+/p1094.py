import heapq
class Solution:
    def carPooling_v1(self, trips, capacity):
        segs = {}
        for trip in trips:
            people = trip[0]
            # Too many people to take
            if people > capacity:
                return False
            # Consider this trip
            for km in range(trip[1], trip[2]):
                if km not in segs:
                    segs[km] = people
                elif segs[km] + people > capacity:
                    return False
                else:
                    segs[km] += people
        return True

    # Second approach based around a priority queue/heap. A min heap does what I need
    def carPooling_v2(self, trips, capacity):
        on, off = [], []
        cap = 0
        for trip in trips:
            on.append((trip[1], trip[0]))
            off.append((trip[2], trip[0]))
        heapq.heapify(on)
        heapq.heapify(off)
        
        while len(on) > 0:
            if off[0][0] <= on[0][0]:
                step = heapq.heappop(off)
                cap -= step[1]
            else:
                step = heapq.heappop(on)
                cap += step[1]
                if cap > capacity:
                    return False
        return True

    # Slightly different approach using sorting and one heap.
    # I wanted to avoid the overhead of creating the heaps but looks like the sorting is a bit slowers
    def carPooling(self, trips, capacity):
        off = []
        cap = 0
        trips.sort(key=lambda  x: x[1])
        
        i=0
        while i < len(trips):
            if len(off) == 0 or trips[i][1] < off[0][0]:
                step = trips[i]
                cap += step[0]
                if cap > capacity:
                    return False
                heapq.heappush(off, (step[2], step[0]))
                i += 1
            else:
                step = heapq.heappop(off)
                cap -= step[1]
        return True


if __name__ == "__main__":
    sol = Solution()
    trips = [[10,5,7],[10,3,4],[7,1,8],[6,3,4]]
    capacity = 24
    print(sol.carPooling(trips, capacity))