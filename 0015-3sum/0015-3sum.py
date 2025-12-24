class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        sn = sorted(nums)
        f, l, r = 0, 1, 2 # f = fixed pointer

        while f <= len(sn) - 3:
            # to help skip duplicate triplets:
            if f > 0 and sn[f] == sn[f - 1]: # if curr f == prev f, will generate/expect same exact triplets
                f += 1
                continue
            
            l = f + 1
            r = len(sn) - 1

            targetSubSum = 0 - sn[f]
            while l < r:
                currSubSum = sn[l] + sn[r]
                if currSubSum < targetSubSum:
                    l += 1
                elif currSubSum > targetSubSum:
                    r -= 1
                else:
                    # found a valid triplet
                    answers.append([sn[f], sn[l], sn[r]])
                    
                    # move pointers in such a way to eliminate duplicate possibilities

                    # move both, otherwise may generate duplicate triplets (since both l,r needed to add correctly)
                    l += 1
                    r -= 1

                    # after moving both, check each new values were not previously seen. if seen, move until find diff
                    while l < r and sn[l] == sn[l - 1]:
                        l += 1
                    while l < r and sn[r] == sn[r + 1]:
                        r -= 1

            f += 1

        return answers