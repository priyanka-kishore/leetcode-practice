class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        # Brute force - O(n^3) - but i correctly figured out the key! only need to satisfy a + b > c
        # for a in range(len(nums) - 2):
        #     for b in range(a+1, len(nums) - 1):
        #         for c in range(b + 1, len(nums)):
        #             if nums[c] >= nums[a] + nums[b]: # if largest side is too big, rest of array is too big so skip
        #                 break
        #             count += 1


        # Efficient - i had same idea (basically opposite logic of brute force key), 
        # start c from end, and do 2-pointer with a + b on opposite ends before c
        # based on a+b>c requirement, the largest b that satisfies it will guarantee that all the previous a's will satisfy it bc they only get bigger
        # if curr b does not satisfy a+b>c requirement (meaning a+b is too small), increment a (to increase a+b)
        for c in range(len(nums) - 1, 1, -1):

            # two-pointer:
            a = 0
            b = c - 1

            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    count += b - a
                    b -= 1
                else:
                    a += 1


        return count