### Sliding Window + Set
​
# Sliding Window
charset = set()
l = 0  # left pointer to calculate length
res = 0
for r in range(len(s)):
while s[r] in charset: # if already in set
charset.remove(s[l])
l += 1
# if is a new / unique character
charset.add(s[r])
res = max(res, r-l+1) # +1 due to zero indexing
return res