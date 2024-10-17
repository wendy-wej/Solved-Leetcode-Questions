class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        maxAns = ans = 0
        while l < len(height) and r > 0:
            #print("l: ",height[l] )
            #print("r: ",height[r] )
            ans = (min(height[l], height[r])) * (r-l)
            #print("ans: ", ans)
            maxAns = max(ans, maxAns)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxAns
         
        