def action(movement, droid, speed, time):
	for move in movement:
		direction = move[0]
		move_times = move[1]
		if direction == 'east':
			droid.roll(0, 90, 0)
			droid.roll(speed, 90, time * move_times)
		elif direction == 'south':
			droid.roll(0, 180, 0)
			droid.roll(speed, 180, time * move_times)
		elif direction == 'west':
			droid.roll(0, 270, 0)
			droid.roll(speed, 270, time * move_times)
		elif direction == 'north':
			droid.roll(0, 0, 0)
			droid.roll(speed, 0, time * move_times)
		else:
			droid.animate(5)
