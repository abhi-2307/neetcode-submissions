class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        result = []
        i = 0
        for i in nums:
            counter[i] = counter.get(i,0) + 1

        sorted_counter = dict(sorted(counter.items(), key=lambda item:item[1], reverse = True))
        temp = list(sorted_counter.keys())
        return temp[:k]
