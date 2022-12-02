class Solution:
    def isValid(self, s: str) -> bool:
        
        hm = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for char in s:
            if char not in hm:
                stack.append(char)
            else:
                if stack and hm[char] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
        
        
        return len(stack) == 0
            

        