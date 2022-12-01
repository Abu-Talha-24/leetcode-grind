class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
        
    
    def alphanum(self, char):
        if (
            ord("a") <= ord(char) <= ord("z")
            or ord("A") <= ord(char) <= ord("Z")
            or ord("0") <= ord(char) <= ord("9")
        ):
            return True
        else:
            return False