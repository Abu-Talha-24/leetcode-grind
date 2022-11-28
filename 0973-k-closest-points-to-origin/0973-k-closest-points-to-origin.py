class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Complexity : O(klogn)
        
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

            
        res = []
        heapq.heapify(pts)  # O(n) 
        
        # Get the lowest(nearest) k points
        for i in range(k):                     # k
            dist, x, y = heapq.heappop(pts)        # log n
            res.append([x, y])
        return res