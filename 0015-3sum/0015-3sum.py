class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []

        nums.sort()
        # print(nums)

        i, j, k = 0, 1, len(nums) - 1

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # print(f"{nums[i]} (i) is duplicate...skipping i")
                continue
            
            # print(nums[i])

            j = i + 1
            k = len(nums) - 1

            while j < k:
                # print(i,j,k)
                if j > i + 1 and nums[j] == nums[j - 1]:
                    # print(f"{nums[j]} (j) is duplicate...skipping j")
                    j += 1
                    continue
                
                remaining_target = 0 - nums[i]
                remaining_sum = nums[j] + nums[k]
                if remaining_sum < remaining_target:
                    # print(f"sum {remaining_sum} too small...moving j")
                    j += 1
                elif remaining_sum > remaining_target:
                    # print(f"sum {remaining_sum} too big...moving k")
                    k -= 1
                else:
                    # print(f"found a triplet: [{nums[i]}, {nums[j]}, {nums[k]}]")
                    answers.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1


        return answers