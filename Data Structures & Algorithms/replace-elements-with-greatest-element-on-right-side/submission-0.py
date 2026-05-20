class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]*len(arr)
        maxi=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            maxi=max(maxi, arr[i+1])
            res[i] = maxi
        return res


        