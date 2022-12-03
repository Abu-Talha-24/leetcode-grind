class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Count Freq of tasks
        freq = Counter(tasks)
        # Make a maxheap - return max element
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        # Make a queue
        q = deque()
        time = 0
        # while the maxheap or q:
        while maxHeap or q:
            # time 
            time += 1
        
            # if maxheap:
            if maxHeap:
                # do the task and add to waiting queue
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt:
                    q.append((cnt,time + n))
                
            # if time arrives:
            if q and q[0][1] == time:
                # add to maxHeap
                heapq.heappush(maxHeap,q.popleft()[0])
        
        # return time
        return time
        