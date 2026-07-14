class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        s=defaultdict(int)
        q=deque()
        freq = Counter(tasks)
        heap = [-v for v in freq.values()]
        heapq.heapify(heap)
        time=0
        while q or heap:
            time+=1
            if heap:
                a=heapq.heappop(heap)
                a=a+1
                if a!=0:
                    q.append((a,time+n))
            if q and q[0][1]==time:
                a,b=q.popleft()
                heapq.heappush(heap,a)
        return time



