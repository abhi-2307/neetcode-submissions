class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = 0
        def recurse(i, total):
            if i == len(nums):
                return total
            return recurse(i+1, total^nums[i]) + recurse(i+1, total)

        return recurse(0,0)


        