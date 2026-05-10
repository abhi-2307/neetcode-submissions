class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        counter = {}
        res = []
        for i in nums:
            counter[i] = counter.get(i,0)+1
        for key, val in counter.items():
            freq[val].append(key)
        for i in range(len(freq)-1, 0, -1):
            if not freq[i]:
                continue
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
