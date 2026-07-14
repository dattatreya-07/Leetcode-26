class Solution(object):
    def sortColors(self, nums):
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)

        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2
