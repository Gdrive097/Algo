import heapq
from typing import List, Tuple, Dict

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, int]:
    """
    graph: adjacency list representation
      graph[u] = list of (v, weight) edges
    Returns distances from source to all reachable nodes.
    """
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    pq = [(0, source)]  # (distance, node)
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for (v, w) in graph.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist
