class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = set()
        for i in nums:
            freq[i] = freq.get(i,0) + 1
            if freq[i] > len(nums)/3:
                res.add(i)
        return list(res)
