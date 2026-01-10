class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        seek_zero = 0
        seek_nonzero = seek_zero + 1

        while seek_nonzero < len(nums):
            while seek_zero < len(nums) - 1 and nums[seek_zero] != 0:
                seek_zero += 1
            
            seek_nonzero = seek_zero
            while seek_nonzero < len(nums) - 1 and nums[seek_nonzero] == 0:
                seek_nonzero += 1
            
            if nums[seek_zero] == 0 and nums[seek_nonzero] != 0:
                nums[seek_zero] = nums[seek_nonzero]
                nums[seek_nonzero] = 0
            
            seek_zero += 1
            seek_nonzero += 1
