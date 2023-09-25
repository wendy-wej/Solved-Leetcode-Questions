class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])
        # ans = ""
        # word = ""
        # for i in s:
        #     if  i != " ":
        #         word+=i
        #     else:
        #         ans+=word[::-1]
        #         ans+=" "
        #         word= ""
        # ans+=word[::-1]
        # return ans
        