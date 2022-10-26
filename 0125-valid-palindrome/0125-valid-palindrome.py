class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_str = ''.join(filter(str.isalnum, s))
        my_str = alnum_str.lower()
        print(my_str)

        my_array = list(my_str)
        print(my_array)

        if not my_array:
            return True

        l = 0
        r = len(my_str)-1


        while l <= r:
            if my_array[l] == my_array[r]:
                palind = True
                l +=1
                r -=1
            else:
                palind = False
                break
        return palind