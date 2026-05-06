class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        result = []
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        hash_map = dict(sorted(hash_map.items(), key=lambda item:item[1], reverse = True))
        return list(hash_map.keys())[:k]
        
        