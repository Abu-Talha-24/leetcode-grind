class Solution:
    def isValid(self, s: str) -> bool:
        
        hm = {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for char in s:
            if char not in hm:
                stack.append(char)
                continue
            if not stack or stack[-1] != hm[char]:
                return False
            stack.pop()
        
        return not stack