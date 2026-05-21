class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        
        itr = self.permute(nums[1:])
        res = []

        for i in itr:
            for j in range(len(i)+1):
                i_copy = i.copy()
                i_copy.insert(j,nums[0])
                res.append(i_copy)
        return res