// Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

// A subarray is a contiguous part of an array.

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map = {0: 1}
        count = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum % k in hash_map:
                count+=hash_map[prefix_sum % k]
            hash_map[prefix_sum%k] = hash_map.get(prefix_sum%k, 0) + 1 
        return count
