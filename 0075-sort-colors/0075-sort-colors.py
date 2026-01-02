import math

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lo = 0
        hi = len(nums) - 1

        if len(nums) == 1:
            return

        i = 0
        while i <= hi:
            # print(nums, nums[i])
            if nums[i] == 1:
                i += 1

            elif nums[i] == 2: # high number
                # swap
                tmp = nums[i]
                nums[i] = nums[hi]
                nums[hi] = tmp

                hi -= 1
                # print(f'HIGH number... swapping and decrementing hi to index {hi}')
                continue
            
            elif nums[i] == 0: # low number
                # swap
                tmp = nums[i]
                nums[i] = nums[lo]
                nums[lo] = tmp
                lo += 1
                i += 1
                # print(f'LOW number... swapping and incrementing lo to index {lo}')
                continue
            
            