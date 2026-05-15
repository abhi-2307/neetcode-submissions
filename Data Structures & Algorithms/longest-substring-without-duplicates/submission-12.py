class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        left = 0
        max_length = 0

        for right in range(len(s)):

            # duplicate inside current window
            if s[right] in visited and visited[s[right]] >= left:
                left = visited[s[right]] + 1

            visited[s[right]] = right

            max_length = max(max_length, right - left + 1)

        return max_length