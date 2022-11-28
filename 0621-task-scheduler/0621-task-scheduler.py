class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # max heap returns the max element
        
        count = Counter(tasks)
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        q = deque()  # paris of [-cnt, idleTime(available t)]
        time = 0
        
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # return the task with highest freq and decrease 1
                if cnt:     # when task becomes 0 skip
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time 
                
        