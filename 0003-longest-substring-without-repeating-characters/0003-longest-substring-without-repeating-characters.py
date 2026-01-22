class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen = {} # char-index pairs {'a': 0 }
        start = 0
        max_len = 0

        for i, char in enumerate(s):
            if char in seen:
                # shrink window start to after the first seen occurrence or `start` (whichever is further right, bc should not move window start backwards!)
                start = max(start, seen[char] + 1)
            
            seen[char] = i # update last seen position
            max_len = max(max_len, i - start + 1) # check length of current window
        
        return max_len