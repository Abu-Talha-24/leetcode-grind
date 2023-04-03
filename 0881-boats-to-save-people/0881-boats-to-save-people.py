class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        res = 0
        
        i = 0
        while i < len(people):
            # total = people[i]
            j = i + 1
            # maximise (i + j) and <= limit , binary search
            l, r = i + 1, len(people) - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2
                total = people[i] + people[mid]
                
                if total > limit:
                    r = mid - 1
                elif total <= limit:
                    idx = mid
                    l = mid + 1
            if idx >= 0:
                people.pop(idx)
            res += 1
            i += 1
                
        
        return res