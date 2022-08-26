class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        word = ''
        for i,char in enumerate(s):
            if char != " ":
                word += char
            else:
                if word :
                    res.append(word)
                    word = ''
        if word:
            res.append(word)
        return " ".join(res[::-1])
        