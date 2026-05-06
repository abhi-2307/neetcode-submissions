class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans =[]
        for i,a in enumerate(nums):
            if a >0: 
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            s, e = i+1, len(nums)-1
            while s<e:
                target = a + nums[s] + nums[e]
                if target > 0:
                    e-=1
                elif target < 0:
                    s+=1
                else :
                    ans.append([a, nums[s], nums[e]])
                    s+=1
                    e-=1
                    while s<e and nums[s]==nums[s-1]:
                        s+=1
        return ans 
        