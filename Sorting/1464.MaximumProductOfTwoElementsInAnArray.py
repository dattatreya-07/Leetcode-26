class Solution(object):
    def maxProduct(self, nums):
        max=0
        smax=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        return (nums[0]-1)*(nums[1]-1)
                       
