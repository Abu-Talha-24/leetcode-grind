class Solution:
def minFlipsMonoIncr(self, s: str) -> int:
def isaMonotone(binstr):
n = len(binstr)
change = False
for i in range(1, n):
if not change and binstr[i] == binstr[i-1]:
continue
elif not change and binstr[i] != binstr[i-1]:
change = True
continue
if binstr[i] != binstr[i-1]:
return False
return True
if isaMonotone(s):
return 0
n = len(s)
first = s[0 : n//2]
second = s[n//2 : n]
fcount, scount = Counter(first), Counter(second)
print(fcount)
return 0
#         fzeros, fones = 0, 0
#         szeroes, sones = 0, 0
#         flips = 0
#         # if first half is ONLY zeroes: (smaller half)
#         if fones == 0:
#             # flip whatever is lowest
#             flips += min(szeroes, sones)
#             return flips
​
#         if fones != 0: