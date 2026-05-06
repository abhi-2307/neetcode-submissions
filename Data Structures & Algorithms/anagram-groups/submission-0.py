class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord("a")]+=1
            hashset[tuple(count)].append(i)
        return hashset.values()



        