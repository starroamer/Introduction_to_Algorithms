# encoding:utf8
"""
有向无环图的对短路径算法
"""
from collections import defaultdict
inf = float('inf')


def dijkstra(a, s, t):
    """
    :param a: adjacent matrix of given graph
    :param s: start node
    :param t: end node
    :return: min distance of s to t
    """
    n = len(a[0])
    dis = defaultdict(lambda: inf)
    dis[s] = 0
    prev = {}
    unknown_set = set(xrange(n))

    while unknown_set:
        """
        dis中的最小值dis[x]就是s到x的最终最短路径长度
        若存在更短的路径，则存在该路径上的节点y，使得dis[y] < dis[x]
        """
        i = None
        for x in unknown_set:
            if dis[x] <= dis[i]:
                i = x
        unknown_set.remove(i)

        # 动态规划更新每个节点的最短路径长度
        for j in xrange(n):
            if j == i or a[i][j] == inf:
                continue
            if dis[i] + a[i][j] < dis[j]:
                dis[j] = dis[i] + a[i][j]
                prev[j] = i

    path = [t]
    prev_node = prev[t]
    while prev_node != s:
        path.insert(0, prev_node)
        prev_node = prev[prev_node]

    path.insert(0, prev_node)

    return path, dis[t]


def dijkstra_test():
    a = [[0, 1, 12, inf, inf, inf],
         [inf, 0, 9, 3, inf, inf],
         [inf, inf, 0, inf, 5, inf],
         [inf, inf, 4, 0, 13, 15],
         [inf, inf, inf, inf, 0, 4],
         [inf, inf, inf, inf, inf, 0]]

    shortest_path, shortest_dis = dijkstra(a, 0, 5)
    print shortest_dis
    print '->'.join(map(str, shortest_path))


if __name__ == "__main__":
    dijkstra_test()