class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)        
        st = []
        
        i = 0
        while i < n:
            if path[i] == '/':
                i += 1
                word = ''
                while i < n and path[i] != '/':
                    word += path[i]
                    i += 1
                if word: st.append(word)
            
            if st:
                if st[-1] == '.':
                    st.pop()
                elif st[-1] == '..':
                    st.pop()
                    if st: st.pop()
                else:
                    continue
        
        res = '/'.join(st)
        res = res.rstrip('/')
        res = '/' + res

        
        return res
        
        