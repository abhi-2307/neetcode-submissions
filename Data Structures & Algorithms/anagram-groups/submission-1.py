from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        result = []
        for i in range(len(strs)):
            counter[tuple(sorted(Counter(strs[i]).items()))].append(strs[i])
        print(counter)
        return list(counter.values())

        