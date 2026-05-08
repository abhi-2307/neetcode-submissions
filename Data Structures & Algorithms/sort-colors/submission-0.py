class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #bubble sort

        for i in range(len(nums)-1):
            swapped = False
            for j in range(len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped =True
                j+=1
            if not swapped:
                break
        return nums
        