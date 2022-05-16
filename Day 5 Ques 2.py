// You are given an integer array nums. 
// You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
// Return true if you can reach the last index, or false otherwise.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal=len(nums)-1
        for i in range(goal,-1,-1):
            if i + nums[i]>=goal:
                goal=i
        return True if goal is 0 else False
