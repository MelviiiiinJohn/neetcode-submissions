class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stk=[]

        for i,t in enumerate(temperatures):
            while stk and stk[-1][0]<t:
                stk_t,stk_i=stk.pop()
                res[stk_i]=i-stk_i
            stk.append((t,i))    
        return res