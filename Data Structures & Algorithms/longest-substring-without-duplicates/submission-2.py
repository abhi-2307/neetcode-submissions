class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hashset = set()
        maxi = 1
        i, j = 0, 1
        while j<len(s):
            
            hashset.add(s[i])
            if s[j] in hashset:
                i+=1
                j=i+1
                hashset.clear()
                continue
            hashset.add(s[j])
            maxi = max(maxi,j-i+1)
            j+=1
        
        return maxi
        