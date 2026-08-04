class Solution(object):
    def findMissingElements(self, nums):
        a=[]
        mi=min(nums)
        ma=max(nums)
        for i in range(mi,ma):
            if i not in nums:
                a.append(i)
        return a
