import itertools
from graph import Graph
from multiple_Astar import A_star

def tsp(G, points):
    path = None
    mini = float('inf')
    n = len(points)
    for per in itertools.permutations(range(1, n)):
        ind_ls = [0] + list(per) +[0]
        iter_ind = [0] + list(per)
        new_path = [points[i] for i in ind_ls]
        dist = 0
        for i in iter_ind:
            dist = dist + len(A_star(G, new_path[i], new_path[i + 1]))
        if dist < mini:
            mini = dist
            path = new_path
    visited_node = []
    for j in range(len(path) - 2):
        visited_node += A_star(G, path[j], path[j + 1])

    return visited_node






