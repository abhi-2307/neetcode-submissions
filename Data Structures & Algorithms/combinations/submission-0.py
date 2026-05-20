class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [_ for _ in range(1,n+1)]
        result = []
        def recurse(i, subset):
            if len(subset)==k:
                result.append(subset.copy())
                return
            if len(subset) >k or i==len(nums):
                return
            subset.append(nums[i])
            recurse(i+1,subset)
            subset.pop()
            recurse(i+1,subset)
        recurse(0,[])
        return result

        