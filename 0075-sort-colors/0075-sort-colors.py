class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        curr = 0
        zero_spot = 0
        two_spot = len(nums) - 1

        while curr <= two_spot:
            if nums[curr] == 2 and curr != two_spot:
                nums[curr] = nums[two_spot]
                nums[two_spot] = 2
                two_spot -= 1
                continue
            
            if nums[curr] == 0 and curr != zero_spot:
                nums[curr] = nums[zero_spot]
                nums[zero_spot] = 0
                zero_spot += 1
                continue
            
            curr += 1
        