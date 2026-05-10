class Solution:
    def merge_sort(self, nums1, nums2):
        i, j =0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums2[j] <= nums1[i]:
                result.append(nums2[j])
                j+=1
            else:
                result.append(nums1[i])
                i+=1
        while i < len(nums1):
            result.append(nums1[i])
            i+=1
        while j < len(nums2):
            result.append(nums2[j])
            j+=1
        nums1[:] = result
        return
        

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            nums1[:] = nums2
            return
        else:
            nums1[:] = nums1[:m]
        self.merge_sort(nums1, nums2)


        