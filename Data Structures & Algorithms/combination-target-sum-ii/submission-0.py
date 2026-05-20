class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result,subset = [],[]
        def recurse(i,k):
            if k==0:
                result.append(subset.copy())
                return
            if k<0 or i ==len(candidates):
                return
            subset.append(candidates[i])
            recurse(i+1,k-candidates[i])
            subset.pop()

            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            recurse(i+1,k)
        recurse(0, target)
        return result
        