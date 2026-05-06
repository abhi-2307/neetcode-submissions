class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        maxf, i = 0, 0
        for j in range(len(s)):
            hashmap[s[j]] = 1 + hashmap.get(s[j], 0)
            maxf = max(maxf,hashmap[s[j]])
            if (j-i+1) - maxf > k :
                hashmap[s[i]]-=1
                i+=1
        return (j-i+1)

        