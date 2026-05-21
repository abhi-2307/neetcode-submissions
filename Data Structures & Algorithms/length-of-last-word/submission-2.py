class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        count=0
        while i >= 0:
            if s[i]==" ":
                i-=1
            else:
                while i >= 0 and s[i]!=" ":
                    count+=1
                    i-=1
                return count

        return 0

        