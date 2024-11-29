import random
class RandomizedSet:

    def __init__(self):
        self.numHashSet = set()
        
        

    def insert(self, val: int) -> bool:
        if val in self.numHashSet:
            return False
        else:
            self.numHashSet.add(val)
            return True
    def remove(self, val: int) -> bool:
        if val not in self.numHashSet:
            return False
        else:
            self.numHashSet.remove(val)
            return True

    def getRandom(self) -> int:
        numList = list(self.numHashSet)
        
        return random.choice(numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()