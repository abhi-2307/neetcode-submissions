class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for i in s:
            chars[i] = 1+chars.get(i,0)
        for j in t:
            if j not in chars:
                return False
            if j in chars:
                chars[j] -= 1
            if chars[j] == 0:
                del(chars[j])
        return len(chars) == 0
        