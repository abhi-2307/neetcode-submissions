class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1
        hash_map = {}
        hash_map[nums[i]] = i
        for i in range(1, len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target- nums[i]], i]
            hash_map[nums[i]] = i
        return [0,0]
        