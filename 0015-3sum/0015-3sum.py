class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array
        # 1 fixed pointer + 2 other pointers to find rest of sum to 0
        # avoid duplicates by:
        #   1. avoiding repeat fixed pointers
        #   2. avoiding repeat left and right pointers after moving each inwards

        nums.sort()
        res = []

        # f stops before last 2 elements
        for f in range(len(nums) - 2):

            # if this f value is same as last, skip to avoid duplicates
            if (f > 0 and nums[f] == nums[f-1]):
                continue

            newTargetSum = 0 - nums[f]

            l = f + 1
            r = len(nums) - 1

            # 2-sum problem, where sum = newTargetSum
            while l < r:
                s = nums[l] + nums[r]

                if s > newTargetSum:
                    r -= 1
                elif s < newTargetSum:
                    l += 1
                else:
                    # found the triplet: add to result array + set next itr pointers
                    res.append([nums[f], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # set up next iteration (l,r pointers) to avoid duplicate triplets
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1
                    while (l < r and nums[r] == nums[r+1]):
                        r -= 1


        return res # array of tuplets of correct items (not indices)