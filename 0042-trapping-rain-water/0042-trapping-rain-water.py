class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l = 0
        r = len(height)-1
        leftMax, rightMax = height[l], height[r]
        rain = 0
      
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                rain += leftMax-height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                rain += rightMax-height[r]
        return rain
                
        
        