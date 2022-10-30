class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
    
    
   ##My Slower Solution 
'''
def isAnagram(s,t):
    for i in list(s):
        if i in t:
            t = t.replace(i, "", 1)
        else:
            return False
    if len(t)!=0:
        return False
    
    return True
print(isAnagram(s,t))
'''