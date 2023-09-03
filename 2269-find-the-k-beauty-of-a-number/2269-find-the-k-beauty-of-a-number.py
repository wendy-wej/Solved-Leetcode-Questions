class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numToArray = str(num)
        l = 0
        r = k
        count = 0
        while (r<=len(numToArray)):
            newnum = int(numToArray[l:r])
            #print("newnum:",newnum)
            if newnum!=0 and(num % newnum==0):
                count +=1
            l +=1
            r +=1
        return count
        

        
        