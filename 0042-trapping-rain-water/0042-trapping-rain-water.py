class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height)-1
        maxL,maxR = height[left], height[right]
        ans = 0
        
        while left < right:
            if maxL < maxR:
                left +=1
                maxL = max(maxL, height[left])
                ans += maxL - height[left]
            
            else:
                right -=1
                maxR = max(maxR, height[right])
                ans += maxR - height[right]
                
        return ans
            
        