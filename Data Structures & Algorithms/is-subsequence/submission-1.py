class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        if len(s)>len(t):
            return False
        if not s:
            return True
        while j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
            if i==len(s):
                return True
        return False
            

        