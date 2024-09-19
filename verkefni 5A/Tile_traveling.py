# Fribbi
# Tile_Traveling
def move_input():
	inp = str(input())
	return inp.upper()
def get_possible_moves(dir, loc):
	for x, y in dir.items():
		if loc == float(x):
			return y
		else:
			continue
def move_North(floatnum):
	return round(float(floatnum)+0.1,1)
def move_east(floatnum):
	return round(float(floatnum)+1,1)
def move_south(floatnum):
	return round(float(floatnum)-0.1,1)
def move_west(floatnum):
	return round(float(floatnum)-1,1)
def possible_and_move(mov_dir,loc,poss):
	if mov_dir in poss:
		if mov_dir == 'N':
			newloc=move_North(loc)
		elif mov_dir == 'W':
			newloc=move_west(loc)
		elif mov_dir == 'E':
			newloc=move_east(loc)
		elif mov_dir == 'S':
			newloc=move_south(loc)
		return newloc
	else:
		print('Not a valid direction!')
		return loc
	
location = float(1.1)
victory = False

while victory == False:
	possible_moves=get_possible_moves(directions,location)
	possible_move_str = []
	print('you can travel:',end=' ')
	for x in possible_moves:
		if x == 'N':
			possible_move_str.append('(N)orth')
		elif x == 'W':
			possible_move_str.append('(w)est')
		elif x == 'E':
			possible_move_str.append('(E)ast')
		elif x == 'S':
			possible_move_str.append('(S)outh')
	print(' or '.join(possible_move_str)+'.')
	print('Direction:')
	move=move_input()
	location=possible_and_move(move,location,possible_moves)
	if location == 3.1:
		victory = True
		print('Victory!')
