import math

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lo = 0
        hi = len(nums) - 1

        i = 0
        while i <= hi:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2: # high number
                nums[i], nums[hi] = nums[hi], nums[i] # swap
                hi -= 1
            elif nums[i] == 0: # low number
                nums[i], nums[lo] = nums[lo], nums[i] # swap
                lo += 1
                i += 1
