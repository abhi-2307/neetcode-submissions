class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def recurse(i):
            if i==len(nums):
                result.append(subset.copy())
                return
            recurse(i+1)
            subset.append(nums[i])
            recurse(i+1)
            subset.pop()
        recurse(0)
        return result
        