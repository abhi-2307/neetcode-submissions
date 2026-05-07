class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,j = 0, len(s)-1
        while i <= j:
            temp_i= s[i]
            s[i], s[j] = s[j], temp_i
            i+=1
            j-=1
        print(s)

        