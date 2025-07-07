class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(1) space
        MAX_NUMS_LEN = (10 ** 5)
        L = R = 0
        min_len = MAX_NUMS_LEN + 1
        cur_sum = nums[L]

        # O(n) time
        while L < len(nums) and R < len(nums):
            if cur_sum < target:
                R += 1
                if R < len(nums):
                    cur_sum += nums[R]
            else:
                min_len = min(R - L + 1, min_len)
                cur_sum -= nums[L]
                L += 1
            
            if min_len == 1:
                return 1
        
        return 0 if min_len > MAX_NUMS_LEN else min_len