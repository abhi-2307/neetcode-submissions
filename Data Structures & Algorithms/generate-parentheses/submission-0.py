class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def recurse(s,o,c):
            if o>c:
                return
            if o==0 and c==0:
                res.append(s)
                return
            
            if o>0:
                recurse(s+"(", o-1, c)

            if c>0:
                recurse(s+")", o, c-1)

        recurse("", n, n)
        return res
        