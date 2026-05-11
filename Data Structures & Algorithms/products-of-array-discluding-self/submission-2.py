class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        right = [0]*len(nums)
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                left[i]=1
                continue
            left[i] = left[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                right[i]=1
                continue
            right[i] = right[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans[i] = left[i]*right[i]
        return ans