class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alnum_str = ''.join(filter(str.isalnum, s)) #removes all non-alphanum and spaces
        my_str = alnum_str.lower() #converts to lowercase
        
        my_array = list(my_str) #make an array
      
        #all empty arrays should return true
        if not my_array: 
            return True

        #my two pointers
        l = 0
        r = len(my_str)-1


        while l <= r:
            if my_array[l] == my_array[r]:
                palind = True
                l +=1
                r -=1
            else:
                palind = False
                break  #no need to continue running
        return palind