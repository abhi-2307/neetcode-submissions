class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        res = []

        perms = self.permuteUnique(nums[1:])

        for p in perms:

            for i in range(len(p) + 1):

                # skip duplicate insertion positions
                if i > 0 and p[i - 1] == nums[0]:
                    break

                p_copy = p.copy()

                p_copy.insert(i, nums[0])

                res.append(p_copy)

        return res