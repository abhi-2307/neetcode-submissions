class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        n = len(nums)
        k = target
        for i in range(n):
            if (k - nums[i]) in track:
                return [track[(k - nums[i])], i]
            track[nums[i]] = i
        return 0
        