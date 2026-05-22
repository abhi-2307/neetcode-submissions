class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        base = strs[0]
        res = ""

        for i in range(len(base)):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or base[i]!=strs[j][i]:
                    return res
            res+=base[i]
        return res
                


        