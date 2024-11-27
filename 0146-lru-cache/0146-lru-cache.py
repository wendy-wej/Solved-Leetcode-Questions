# Node has 4 component: key, value, next and prev
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #This maps keys to the node
        
        self.left = Node(0,0)
        self.right =Node(0,0)
        
        self.right.prev =self.left
        self.left.next = self.right 
        
    # Insers at the right to become the LRU
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right
        
        prev_node.next = next_node.prev = node
        node.prev, node.next  = prev_node, next_node

    
    # Removes 
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next        
        prev_node.next, next_node.prev = next_node, prev_node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) #Make it the MRU
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        #Put it in
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)   #Add to hashmap
        self.insert(self.cache[key])         #Add to linked list
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)            #remove from LL
            del self.cache[lru.key]     #Remove from hashmap
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)