class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n > 0 and n not in visited:
            visited.add(n)
            num_str = str(n)
            n = 0
            for i in range(len(num_str)):
                n += int(num_str[i])**2
            # print(n)
            if n == 1:
                return True
            elif n<5:
                return False
        return False
        
        