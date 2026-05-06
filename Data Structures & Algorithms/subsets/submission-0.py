class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        ans = []
        def f(i):
            if i>=len(nums):
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            f(i+1)
            temp.pop()
            f(i+1)
        f(0)
        return ans
        