class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0

        stop_to_bus = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].append(bus)
        
        visited_bus = set()
        q = deque([source]) # stops in the queue
        buses = 0

        while q:
            size = len(q)
            buses += 1

            for _ in range(size):
                curr_stop = q.popleft()
                if curr_stop not in stop_to_bus:
                    return -1
                for bus in stop_to_bus[curr_stop]:
                    if bus in visited_bus:
                        continue
                    visited_bus.add(bus)
                    for stop in routes[bus]:
                        if stop == target:
                            return buses
                        q.append(stop)
        
        return -1