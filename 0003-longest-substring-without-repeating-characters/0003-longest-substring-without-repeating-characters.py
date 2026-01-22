class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen = {} # char-index pairs {'a': 0 }
        start = 0
        max_len = 0

        for i in range(len(s)):

            if s[i] not in seen:
                seen[s[i]] = i # add to set
                max_len = max(max_len, i - start + 1) # check max_len
            else:
                # re-adjust window: move start to index AFTER first seen occurrence
                start = seen[s[i]] + 1

                # don't forget to REMOVE dict elements where value < index of first seen occurrence
                seen = {char: index for char, index in seen.items() if index >= seen[s[i]]}
                # and update index of repeated occurrence
                seen[s[i]] = i

                # don't forget to recalc that new length after moving start forward
                max_len = max(max_len, i - start + 1)
        
        return max_len