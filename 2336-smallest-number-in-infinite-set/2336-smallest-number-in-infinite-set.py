class SmallestInfiniteSet:

    def __init__(self):
        # self.arr = []
        self.small_count = 1
        self.num_removed = set()
        

    def popSmallest(self) -> int:
        if self.num_removed:
            count = min(self.num_removed)
            self.num_removed.remove(count)
            return count
        else:
            self.small_count +=1
            return self.small_count-1
        
    def addBack(self, num: int) -> None:
        if self.small_count > num:
            self.num_removed.add(num) 


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)