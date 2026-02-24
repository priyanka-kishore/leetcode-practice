class Solution:
    def decodeString(self, s: str) -> str:
        sequence = ""
        stack = []

        for c in s:
            if c != ']':
                # add character to stack
                stack.append(c)
            else:
                # collect string inside brackets
                encoded_string = ""
                ch = stack.pop()
                while ch != '[':
                    encoded_string = ch + encoded_string
                    ch = stack.pop()

                # collect frequency (integer 0-300) before brackets
                freq = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    n = stack.pop()
                    freq = n + freq

                encoded_string *= int(freq)
                stack.append(encoded_string)
                    
        # handle any remaining characters left in stack
        if len(stack) > 0:
            sequence += "".join(stack)
        
        return sequence