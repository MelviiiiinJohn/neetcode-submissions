class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)

        def bs(target):
            l,r=0,n
            while l<r:
                m=(l+r)//2
                if nums[m]>=target:
                    r=m
                else:
                    l=m+1
            return l

        start=bs(target)     
        if start==n or nums[start]!=target:
            return [-1,-1]
        return [start, bs(target + 1) - 1]