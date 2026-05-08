class Solution:
    def merge(self, left, right):
        i, j, sorted = 0,0,[]
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                sorted.append(right[j])
                j+=1
            else:
                sorted.append(left[i])
                i+=1
        while i < len(left):
            sorted.append(left[i])
            i+=1
        while j < len(right):
            sorted.append(right[j])
            j+=1
        return sorted
            
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #merge sort
        if len(nums) <=1:
            return
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        self.sortColors(left)
        self.sortColors(right)
        merged = self.merge(left, right)
        nums[:] = merged

        