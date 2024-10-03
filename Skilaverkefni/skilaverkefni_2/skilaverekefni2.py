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
	if 0 < placeInLine < 11:
		placeInLine -= 1
		break

while True:
	print(''.join('o' if x == placeInLine else 'x' for x in range(10)))
	print('l: left\nr: right')

	print('Move:')
	move = input().lower()

	if move == 'q':
		break
	elif move == 'r' and placeInLine < 9:
		placeInLine += 1
	elif move == 'l' and placeInLine > 0:
		placeInLine -= 1