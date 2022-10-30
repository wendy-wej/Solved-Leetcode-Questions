class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = deque()
    

        reference = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        for i in s:
            if i in reference.values():
                open_stack.append(i)
            elif i in reference.keys():
                if open_stack and open_stack[-1] == reference[i]:
                    open_stack.pop()
                else:
                    return False

        if len(open_stack) == 0:
            return True
        else:
            return False
        