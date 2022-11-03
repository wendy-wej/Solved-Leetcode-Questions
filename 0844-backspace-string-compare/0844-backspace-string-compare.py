class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = deque()
        b = deque()
        for i in s:
            if i == '#' and len(a) == 0:
                continue
            elif i == '#':
                a.pop()
            else:
                a.append(i)

        for j in t:
            if j == '#' and len(b) == 0:
                continue
            elif j == '#':
                b.pop()
            else:
                b.append(j)

        if a == b:
            return True
        else:
            return False