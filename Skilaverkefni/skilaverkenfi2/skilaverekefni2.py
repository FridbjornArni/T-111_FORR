# Friðbjörn - Tiago
# b.17.9.24
# Skilaverkefni 2 

# rebuild x line

# check if possible to move

# def move right

# def move left


while True:
	print('Position in [1..10]:')
	placeInLine = int(input())
	if placeInLine > 0 and placeInLine < 11:
		placeInLine -= 1
		break
	else:
		continue

while True:
	for x in range(10):
		if x == placeInLine:
			print('o',end='')
		else:
			print('x',end='')
	print()
	print('l: left')
	print('r: right')
	move = str(input('Move: '))
	if move.lower() == 'q':
		break
	elif move.lower() == 'r' and placeInLine < 9: placeInLine += 1
	elif move.lower() == 'l' and placeInLine > 0: placeInLine -=1
	else: continue