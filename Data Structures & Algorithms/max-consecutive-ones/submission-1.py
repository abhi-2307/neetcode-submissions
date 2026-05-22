class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i,j, maxi=0,0,0
        while j<len(nums):
            if nums[i]==0:
                i+=1
                j+=1
            else:
                if nums[j]==0:
                    j+=1
                    i=j
                else:
                    maxi = max(maxi, (j-i+1))
                    j+=1
        return maxi
                
        