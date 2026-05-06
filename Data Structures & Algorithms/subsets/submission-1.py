class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(idx, subset):
            if idx == len(nums):
                result.append(subset.copy())
                return
            dfs(idx+1, subset)
            subset.append(nums[idx])
            dfs(idx+1, subset)
            subset.pop()
        dfs(0, [])
        return result
        