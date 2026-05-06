class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        def f(i,target):
            if target==0:
                ans.append(temp.copy())
                return
            if i>=len(nums) or target<0:
                return
            
            temp.append(nums[i])
            f(i,target-nums[i])
            temp.pop()
            f(i+1,target)
        f(0,target)
        return ans
        
        