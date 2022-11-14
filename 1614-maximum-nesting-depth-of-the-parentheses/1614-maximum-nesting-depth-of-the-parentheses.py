class Solution:
    def maxDepth(self, s: str) -> int:
        closed_counter = 0
        max_closed_counter =0
        for i in s:
            if i == '(':
                closed_counter +=1
            if i == ')':
                max_closed_counter = max(closed_counter, max_closed_counter)
                closed_counter -=1
            else:
                continue
        return max_closed_counter