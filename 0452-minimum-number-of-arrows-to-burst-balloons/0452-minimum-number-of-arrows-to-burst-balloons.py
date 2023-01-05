class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

            
        points.sort(key=lambda x : x[0])
        res = []
        prev = []
        
        # combine the intervals with overlapping co-ords
        for i in range(len(points)):
            if i == 0:
                prev = points[0]
                res.append(prev)
                continue
            if points[i][0] <= prev[1]: # has overlapping
                pt = [points[i][0], min(prev[1], points[i][1])]  # 0 is sorted but 1 isn't so choosing min
                res[-1] = pt # replace the last one as it is overlapped
                prev = pt
            else:
                prev = points[i]
                res.append(prev)
        
        
        #return the length of the points array
        print(res)
        return len(res)