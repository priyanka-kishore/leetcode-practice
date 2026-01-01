class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        nz = 0

        # print(nums)
        while nz < len(nums) - 1:
            # find next 0
            while nums[z] != 0 and z < len(nums) - 1:
                z += 1
            # print(f"found next 0 at index {z}: {nums[z]}")
            
            nz = z # find non-0 after the 0
            while nums[nz] == 0 and nz < len(nums) - 1:
                nz += 1
            # print(f"found next non-0 at index {nz}: {nums[nz]}")
            
            # swap
            if nums[z] == 0 and nums[nz] != 0:
                nums[z] = nums[nz]
                nums[nz] = 0
                # print("swapping...\n", nums)