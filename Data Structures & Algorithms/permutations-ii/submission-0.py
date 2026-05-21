class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]

        res = []

        perms = self.permuteUnique(nums[1:])

        for p in perms:
            for i in range(len(p)+1):
                p_copy=p.copy()
                if i < len(p) and p[i]==nums[0]:
                    continue
                p_copy.insert(i,nums[0])
                if p_copy not in res:
                    res.append(p_copy)
        return res