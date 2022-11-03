from collections import deque
class MyQueue:
    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        self.PutBackInsideFront()
        return self.front.pop()
        

    def peek(self) -> int:
        self.PutBackInsideFront()
        return self.front[-1]

    def empty(self) -> bool:
        self.PutBackInsideFront()
        return len(self.front) == 0

    def PutBackInsideFront(self):
        if not self.front:
            for i in range(len(self.back)):
                self.front.append(self.back.pop())
        return self.front

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()