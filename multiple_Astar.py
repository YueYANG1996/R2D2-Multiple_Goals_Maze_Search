import math
import queue
def A_star(G, start, goal):
    rows = G.vertics[-1][0]
    cols = G.vertics[-1][1]
    node_visited = []
    q = queue.PriorityQueue()
    astar_cost_start = math.sqrt(pow(start[0] - goal[0],2) + pow(start[1] - goal[1],2))
    cost_start = 0
    path = [start]
    q.put((astar_cost_start, cost_start, path, start))
    
    while q.empty() != True:
        current_node = q.get()
        astar_cost, current_cost, path, current_pos = current_node[0], current_node[1], current_node[2], current_node[3]
        
        if current_pos == goal:
            return path

        if current_pos not in node_visited:
            node_visited.append(current_pos)
            for node in G.neighbors(current_pos):
            	expand_cost = current_cost + math.sqrt(pow(node[0] - current_pos[0],2) + pow(node[1] - current_pos[1],2))
            	heuristic = math.sqrt(pow(node[0] - goal[0],2) + pow(node[1] - goal[1],2))
            	expand_astar_cost = expand_cost + heuristic
            	new_state = (expand_astar_cost, expand_cost, path + [node], node)
            	q.put(new_state)
    pass