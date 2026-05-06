class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        result = 1
        if not nums:
            return 0
        for i in nums:
            hash_set.add(i)
        for i in range(len(nums)):
            if nums[i]-1 in hash_set:
                j= 1 
                length = 1
                while nums[i]-j in hash_set:
                    length = length + 1
                    result = max(length, result)
                    j+=1
        return result


        