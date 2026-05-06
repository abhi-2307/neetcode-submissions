class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        res = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] in hash_set:
                hash_set.clear()
                i+=1
                j=i
            else:
                hash_set.add(s[j])
                res = max(res, j-i+1)
                j+=1
        return res
            