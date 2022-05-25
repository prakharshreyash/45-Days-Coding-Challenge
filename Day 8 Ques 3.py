# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        c1 = nums[-1]*nums[-2]*nums[-3]
        c2 = nums[0]*nums[-1]*nums[1]
        
        res = max(c1,c2)
        return res
