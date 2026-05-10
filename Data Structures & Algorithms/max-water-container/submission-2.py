class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i,j = 0,len(heights)-1
        while i < j:
            area = min(heights[i], heights[j])*(abs(i-j))
            max_area = max(max_area, area)
            if heights[j] > heights[i]:
                i+=1
            else:
                j-=1
        return max_area
        