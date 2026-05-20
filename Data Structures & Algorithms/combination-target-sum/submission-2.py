class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result,subset =  [],[]
        def recurse(i, k):
            if k < 0 or i==len(nums):
                return
            if k==0:
                if subset not in result:
                    result.append(subset.copy())
                    return
            recurse(i+1,k)
            subset.append(nums[i])
            recurse(i,k-nums[i])
            subset.pop()
        recurse(0,target)
        return result

        