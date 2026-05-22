class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, maxi = 0,0

        for i in nums:
            if i==1:
                count+=1
                maxi=max(maxi,count)
            if i==0:
                count=0
        return maxi 
                
        