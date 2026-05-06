class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(idx, subset):
            if idx == len(nums):
                result.append(subset.copy()) #Functions don’t get a fresh list unless you explicitly create one, because they all point to the same memory address.
                return
            dfs(idx+1, subset)
            subset.append(nums[idx])
            dfs(idx+1, subset)
            subset.pop()
        dfs(0, [])
        return result
        