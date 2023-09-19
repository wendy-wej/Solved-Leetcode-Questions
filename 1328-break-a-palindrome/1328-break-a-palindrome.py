class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return "" # only case where returning empty string
        for i in range(0, n//2): # go to half of the string only
            if palindrome[i] != "a": return palindrome[0:i]+"a"+palindrome[i+1:]
        return  palindrome[0:-1] +"b"
            
        
        
        
        
        
        
        
        
#         my_list = list(palindrome)
        
#         num = len(my_list)
#         if num==1:
#             return ""
        
#         if palindrome == "aa":
#             return 'ab'
        
#         for i in range(num):
#             if (my_list[i] != "a") and (i!=(num-1)):
#                 my_list[i] ="a"
#                 return "".join(my_list)
        
#         return "".join(my_list)