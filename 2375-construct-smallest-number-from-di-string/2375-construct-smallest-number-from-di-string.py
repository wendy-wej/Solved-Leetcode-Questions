class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        stack = []
        for i, ltr in enumerate(pattern+'I', 1):
            stack.append(str(i))
            if ltr == "I":
                ans += stack[::-1]
                stack = []
        return "".join(ans)
            
        