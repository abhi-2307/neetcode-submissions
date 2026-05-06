class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        base = strs[0]
        for i in range(len(base)):
            for j in range(len(strs)):
                if i >= len(strs[j]) or base[i] != strs[j][i]:
                    return ans
            ans+=base[i]
        return ans
        

        