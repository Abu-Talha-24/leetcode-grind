class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        
        maxHeap = []
        heapq.heapify(maxHeap)
        
        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(x**2 + y**2)
            tup = (-dist, [x,y])
            heapq.heappush(maxHeap, tup)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        for point in maxHeap:
            res.append(point[1])
        
        return res
        