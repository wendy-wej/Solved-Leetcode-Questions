class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #count each character in t
        t = Counter(t)
        
        #setup counter to search t in s
        count = Counter()
        length = len(s)
        
        left = 0
        ans = [length, '']
        string = ''
        
        for index, char in enumerate(s):#use sliding window to find t in s
            
            #keep moving the right pointer
            string += char
            if t[char]:
                count[char] += 1
            
            while t <= count:#if every character in t is found in the string minimize window
                ans = min(ans, [(index - left), string[left:]])#update the answer with minimum length string
                
                if t[s[left]]:
                    count[s[left]] -= 1
                
                left += 1
        return ans[1]
                
        
        
        