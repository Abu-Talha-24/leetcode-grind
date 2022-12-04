class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(len(strs)):
                print(char)
                if len(strs[j]) > i and strs[j][i] != char:
                    return res
                elif len(strs[j]) <= i:
                    return res
                
            res += char        
        return res
        