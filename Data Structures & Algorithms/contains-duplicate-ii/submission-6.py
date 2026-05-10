class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i,visited = 0,{}
        while i < len(nums):
            if nums[i] in visited:
                if abs(i - visited[nums[i]])<=k:
                    return True
            visited[nums[i]] = i
            i+=1
        return False
