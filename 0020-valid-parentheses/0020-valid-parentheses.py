class Solution:
    def isValid(self, s: str) -> bool:
        
        hm = {")": "(",
	         "]": "[",
	         "}": "{"}   
        
        st = []
        
        for char in s:
            if char not in hm:
                st.append(char)
            elif st and hm[char] == st[-1]:
                st.pop()
            else:
                return False
        
        return not len(st)
                
                