class Solution:
    def isValid(self, s: str) -> bool:
        hm={
            ")": "(",
            "]": "[",
            "}": "{"
        }
        st=[]
        for c in s:
            if c in hm:
                if not st:
                    return False
                top=st.pop()
                if top!=hm[c]:
                    return False
            else:
                st.append(c)    
        return len(st)==0          