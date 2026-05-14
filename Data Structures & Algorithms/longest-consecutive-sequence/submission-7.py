class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = {}
        for i in range(len(nums)):
            visited[nums[i]] = i
        max_length = 0
        for i in range(len(nums)):
            length = 1
            while nums[i]-length in visited:
                length+=1
            max_length = max(max_length, length)
        return max_length
            

