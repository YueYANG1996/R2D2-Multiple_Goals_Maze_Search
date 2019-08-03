# R2D2-Multiple_Goals_Maze_Search
This project was the term project of CIS 521 Artificial Intelligence at UPENN.
The Project include two parts -- 8-Puzzle Game & Multiple Goads Maze Search
The demo could be watch in: https://www.yueyang.host/copy-of-3d-reconstruction

The set-up process of the working enviroment in MacOS is available on: http://artificial-intelligence-class.org/r2d2_assignments/hw1/homework1.html

This project combine the A star and Traveling Salesman Algorithm to generate the shortest path between multiple goals and visualized it on R2D2 platform.

#Function Description#

graph.py -- input the vertices and edges to generate a map

multiple_Astar.py -- common A star algorithm to calculate the shortest path between two points

tsp.py -- input the start and goals to reach, using traveling salesman algorthm to compute the best order

r2d2_action.py r2d2_move.py -- convert the path to commands of actual robots
