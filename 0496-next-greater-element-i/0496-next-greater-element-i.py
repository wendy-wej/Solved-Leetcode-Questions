class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums_stack1 = deque(nums1)
        while len(nums_stack1) > 0:
            x = nums_stack1.popleft()
            i = nums2.index(x)
            if i == len(nums2)-1:
                stack.append(-1)
            else:
                for j in nums2[i+1:]:
                    if j > x :
                        stack.append(j)
                        break
                    elif j == nums2[-1]:
                        stack.append(-1)
                    else:
                        continue

        return stack