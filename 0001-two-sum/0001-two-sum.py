class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) space
        seen = {}

        # O(n) time
        for i, n in enumerate(nums):
            if target-n in seen:
                return [seen.get(target-n), i]
            else:
                seen.update({n:i})
        
        return [None,None]