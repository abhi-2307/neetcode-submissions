class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(idx, subset, k):
            if k<0 or idx == len(nums):
                return
            if k==0:
                result.append(subset.copy())
                return
            dfs(idx+1, subset, k)
            subset.append(nums[idx])
            dfs(idx, subset, k-nums[idx])
            subset.pop()
        dfs(0, [], target)
        return result
        
        