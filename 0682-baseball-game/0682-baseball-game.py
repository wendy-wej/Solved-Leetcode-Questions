class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
    
        for i in operations:
            if i == 'D':
                new_ans = stack[-1] * 2
                stack.append(new_ans)
            elif i =="C":
                stack.pop()
            elif i == "+":
                new_ans = stack[-1] + stack[-2]
                stack.append(new_ans)
            else:
                stack.append(int(i)) 
        return(sum(stack))