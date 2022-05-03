// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

// You must solve this problem without using the library's sort function.

 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, len(nums)-1, len(nums) -1
        while i <= j:
            if nums[j] == 1:
                j-=1
            elif nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                j-=1
                k-=1
