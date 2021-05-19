import heapq
from collections import defaultdict


class Edge(object):

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    # For heapq.
    def __cmp__(self, other):
        return __cmp__(self.weight, other.weight)


class Graph(object):

    def __init__(self):
        # 邻接表
        self.adj = defaultdict(list)

    def add_e(self, start, end, weight=0):
        self.adj[start].append(Edge(start, end, weight))

    def s_path(self, src):
        """
        返回从源到数组的每个顶点的距离，该数组表示在索引i处访问节点i之前访问的节点(dist, previous).
        """
        dist = {src: 0}
        visited = {}
        previous = {}
        queue = []
        heapq.heappush(queue, (dist[src],src))
        while queue:
            distance, current = heapq.heappop(queue)
            if current in visited:
                continue
            visited[current] = True

            for edge in self.adj[current]:
                relaxed = dist[current] + edge.weight
                end = edge.end
                if end not in dist or relaxed < dist[end]:
                    previous[end] = current
                    dist[end] = relaxed
                    heapq.heappush(queue, (dist[end],end))
        return dist, previous
