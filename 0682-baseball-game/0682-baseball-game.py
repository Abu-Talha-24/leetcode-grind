class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        ops = operations
        n = len(ops)
        st = []
        
        for i in range(n):
            val = ops[i]
            if val == 'C':
                st.pop()
            elif val == 'D':
                st.append(st[-1] * 2)
            elif val == '+':
                st.append(st[-1] + st[-2])
            else:
                st.append(int(val))

        return sum(st)
            
        
        