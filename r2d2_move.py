def move(path):
	movement = []
	for i in range(len(path) - 1):
		current_node = path[i]
		next_node = path[i + 1]
		vector = (next_node[0] - current_node[0], next_node[1] - current_node[1])
		if vector == (1, 0):
			movement.append('south')
		elif vector == (0, 1):
			movement.append('east')
		elif vector == (0, -1):
			movement.append('west')
		elif vector == (-1, 0):
			movement.append('north')
		else:
			movement.append('stay')
	new_movement = []
	direction = movement[0]
	times = 1
	for j in range(len(movement) - 1):
		j = j + 1
		current_direction = movement[j]
		if current_direction != direction:
			new_movement.append((direction, times))
			direction = current_direction
			times = 1
		else:
			times += 1
	new_movement.append((direction, times))
	return new_movement