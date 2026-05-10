class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            s, e = i+1,len(nums)-1
            while s < e:
                if nums[s] + nums[e] + nums[i] == 0:
                    result.append([nums[i], nums[s], nums[e]])
                    s+=1
                    e-=1
                    while s<e and nums[s] == nums[s-1]:
                        s+=1
                    while e>s and nums[e] ==nums[e+1]:
                        e-=1
                elif nums[s] + nums[e] + nums[i] < 0:
                    s+=1
                else:
                    e-=1
        return result
            