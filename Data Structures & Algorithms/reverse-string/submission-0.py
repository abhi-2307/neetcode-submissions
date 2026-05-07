class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,j = 0, len(s)-1
        while i <= j:
            temp_i, temp_j = s[i], s[j]
            s[i], s[j] = temp_j, temp_i
            i+=1
            j-=1
        print(s)

        