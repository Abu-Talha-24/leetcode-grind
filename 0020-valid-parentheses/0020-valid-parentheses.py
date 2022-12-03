class Solution:
    def isValid(self, s: str) -> bool:
        
        hm = {")": "(",
              "]": "[",
              "}": "{"}
        stack = []
        
        for char in s:
            if char not in hm:
                stack.append(char)
            else:
                if stack and stack[-1] == hm[char]:
                    stack.pop()
                else:
                    stack.append(char)
        
        return len(stack) == 0
                
