class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def recurse(i, subset):
            if i==len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            recurse(i+1,subset)
            subset.pop()

            while i<len(nums)-1 and nums[i+1]==nums[i]:
                i+=1
            recurse(i+1,subset)
        recurse(0,[])

        return res