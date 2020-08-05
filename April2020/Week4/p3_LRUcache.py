'''
There are a couple interesting pieces here.
-Item has a key and a value when put into the cache. The key is used to access the item, which returns a value
-The key doesn't have anything to do with the position in the cache (e.g. cache could have capacity of 2 and you can use 3 as a key)
-There's no remove method. Stuff just gets bumped when the cache is full
-When something is put into the full cache, it knocks out the least recently used item in the cache
==
-Get uses an index to return a value, otherwise returns -1. That sounds like a hashtable behaviour to me
-Need to track when items in cache were last used so we can properly bump the right item. Putting and getting refresh it
>This is the key challenge
-I can keep track of current max priority int, and assign that to the most recently accessed item. That way I can just scan
for the lowest priority item and remove it, without worrying about refreshing every other item's priority after an access
==
This can be greatly improved with a second version
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.fill = 0 # track how many items are in cache
        self.prio = 1 # current priority
        self.min_prio = 1
        self.cache = {} # key, [value, prio]
        self.pk = {}    # priority, key

    def update(self):
        self.prio += 1
        self.min_prio = min(self.pk.keys())
    
    def get(self, key: int) -> int:
        try:
            val = self.cache[key][0]
            prio = self.cache[key][1]
            # Update the priority-key combo
            self.pk.pop(prio, None)
            self.pk[self.prio] = key
            # Update the cache
            self.cache[key][1] = self.prio
            self.update()

            print(f'Cache: {self.cache}, prio: {self.prio}')
            return val
        except:
            print(f'Cache: {self.cache}, prio: {self.prio}')
            return -1
        

    def put(self, key: int, value: int) -> None:
        # My question interpretation: set value of key if key is there,
        # If cache isn't full yet then just add it in. Once full it can never get un-full
        print(f'Putting: {self.cap}')
        # if the key is not in the cache already then need to kick one out
        if key not in self.cache:
            if self.fill < self.cap:
                self.fill += 1
            else:
                rem_key = self.pk[self.min_prio]
                self.cache.pop(rem_key, None)
                self.pk.pop(self.min_prio, None)
        # If the key does exist, we need to remove it from the prio-key before re-adding
        else:
            prio = self.cache[key][1]
            self.pk.pop(prio, None)

        # Add it into cache and the prio-key dict
        self.cache[key] = [value, self.prio]
        self.pk[self.prio] = key
        self.update()
        print(f'Cache: {self.cache}, prio: {self.prio}')


if __name__ == "__main__":
    cache = LRUCache(10)
    cache.put(10, 13)
    cache.put(3, 17)
    cache.put(6, 11)
    cache.put(10, 5)
    cache.put(9, 10)
    print(cache.get(13))
    cache.put(2, 19)
    print(cache.get(2))
    print(cache.get(3))
    # "put","get","put","put","put","get","put","get","get","get",
    # [5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8]
    cache.put(5, 25)
    print(cache.get(8))
    cache.put(9, 22)
    cache.put(5, 5)
    cache.put(1, 30)
    print(cache.get(11))
    cache.put(9, 12)
    print(cache.get(7))
    print(cache.get(5))
    print(cache.get(8))
    # "get","put","put","get","get","get","put","put","get","put",
    # [9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],
    print(cache.get(9))
    cache.put(4, 30)
    cache.put(9, 3)
    print(cache.get(9))
    print(cache.get(10))
    print(cache.get(10))

    # ["LRUCache","put","put","put","put","put","get","put","get","get",
    # "put","get","put","put","put","get","put","get","get","get",
    # "get","put","put","get","get","get","put","put","get","put",
    # "get","put","get","get","get","put","put","put","get","put",
    # "get","get","put","put","get","put","put","put","put","get",
    # "put","put","get","put","put","get",
    # "put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put",
    # "put","get","put","put","put","put","get","get","get","put","put","put",
    # "get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put",
    # "put","put","put","put"]
    # [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],
    # [5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8]
    # [9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],
    # [8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6]
    # ,[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],
    # [3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],
    # [9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],
    # [9,26],[13,28],[11,26]]