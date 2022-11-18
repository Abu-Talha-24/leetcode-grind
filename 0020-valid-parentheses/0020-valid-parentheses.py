class Solution:
    def isValid(self, s: str) -> bool:
        
        
        st = []
        
        for char in s:
            if len(st) > 0:
                if char == ')' and st[-1] == '(':
                    st.pop()
                elif char == ']' and st[-1] == '[':
                    st.pop()
                elif char == '}' and st[-1] == '{':
                    st.pop()
                else:
                    st.append(char)
            else:
                st.append(char)
        
        return len(st) == 0