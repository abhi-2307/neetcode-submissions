class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        x = ""
        while i <len(s) and j<len(t):
            if s[i]==t[j]:
                x+=s[i]
                i+=1
                j+=1
            else:
                j+=1
        return s==x
            

        