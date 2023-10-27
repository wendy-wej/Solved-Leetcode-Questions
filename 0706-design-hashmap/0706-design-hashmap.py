class MyHashMap:

    def __init__(self):
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]
        
        

    def put(self, key: int, value: int) -> None:
        bucket, index = self.getIndex(key)
        if index <0:
            bucket.append((key, value))
        else:
            bucket[index] = (key, value)
    
        
        

    def get(self, key: int) -> int:
        bucket, index = self.getIndex(key)
        if index < 0:
            return -1
        else:
            return bucket[index][1]
                          
    def remove(self, key: int) -> None:
        bucket, index = self.getIndex(key)
        if index <0:
            return 
        else:
            return bucket.remove(bucket[index])
        
    def getIndex(self, key):
        hashKey = key % self.size
        our_bucket = self.buckets[hashKey]
        
        for i, (k,v) in enumerate(our_bucket):
            if k == key:
                return our_bucket, i 
        return our_bucket, -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)