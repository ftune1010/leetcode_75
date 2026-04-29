import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.start = 1
        self.addedSet = set()
        self.added = []
        
    def popSmallest(self) -> int:
        if len(self.added):
            num = heapq.heappop(self.added)
            self.addedSet.remove(num)
            return num
        else:
            self.start += 1
            return self.start - 1

    def addBack(self, num: int) -> None:
        if num < self.start and num not in self.addedSet:
            heapq.heappush(self.added, num)
            self.addedSet.add(num)

        

if __name__ == "__main__":
    obj = SmallestInfiniteSet()
    print(obj.addBack(2))
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.addBack(1))
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())

