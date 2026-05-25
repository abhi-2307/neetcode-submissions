class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for ind, val in enumerate(nums):
            if target-val in track:
                return [track[target-val], ind]
            track[val] = ind
        return []