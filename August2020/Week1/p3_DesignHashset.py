class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.set


if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(10)
    obj.add(10)
    obj.remove(10)
    print(obj.contains(10))