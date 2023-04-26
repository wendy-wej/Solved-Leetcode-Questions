class Solution:
    def addDigits(self, num: int) -> int:
        splitter = [int(x) for x in str(num)]
        total = 0
        for i in range(len(splitter)):
            total += splitter[i]
        if total == 10:
            return 1
        if total < 10:
            return total
        else:
            return self.addDigits(total)