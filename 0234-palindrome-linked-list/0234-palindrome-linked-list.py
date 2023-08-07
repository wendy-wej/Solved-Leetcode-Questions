# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
    
#         slow = head
#         fast = head
        
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
# #         prev = slow
# #         slow = slow.next
# #         prev.next = None
        
# #         while slow:
# #             slow.next = prev
# #             prev = slow
# #             slow = slow.next
# #         fast = head
# #         slow = prev
#         previous = slow
#         while slow:
#             temp = slow.next
#             slow.next = previous
#             previous = slow
#             slow = temp
       
#         fast = head
#         slow = previous
#         while slow:
#             if fast.val != slow.val: 
#                 return False
#             fast, slow = fast.next, slow.next
#         return True
        
        
        
        
        
#         if current.next == None:
#             return True
        
        
        
#         if current.next.next == None:
#             if current.val == current.next.val:
#                 return True
#             else:
#                 return False
            
#         slow = current.next
#         fast = current.next.next
        
#         while fast:
#             slow = slow.next
#             fast = fast.next
            
        
#         previous = slow
#         while slow:
#             temp = slow.next
#             slow.next = previous
#             previous = slow
#             slow = temp
            
#         while current and slow:
#             if slow != current:
#                 return False
#             slow = slow.next
#             current = current.next
            
#         return True
            
            
        