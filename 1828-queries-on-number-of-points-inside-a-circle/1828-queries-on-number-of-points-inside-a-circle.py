
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        res = []
        for circle in queries:
            count = 0    
            x1, y1 = circle[0], circle[1]
            r = circle[2]
            print(circle)
            for point in points:
                x2, y2 = point[0],point[1]
                dis = math.sqrt( pow(x2-x1,2) + pow(y2-y1,2) )
                if dis <= r:
                    count += 1
            
            res.append(count)
        
        return res
                    
                
        