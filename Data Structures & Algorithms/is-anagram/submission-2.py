class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hashset_A = {}
        hashset_B = {}
        for i in range(len(s)):
            hashset_A[s[i]] = 1+ hashset_A.get(s[i],0)
            hashset_B[t[i]] = 1+ hashset_B.get(t[i],0)
        print(hashset_A)
        print(hashset_B)
        return hashset_A == hashset_B
        