# Friðbjörn
# skilaverkefni 1 
# sub id = https://ru.kattis.com/courses/T-111-PROG/PROG24/assignments/xugtn7/submissions/14237657

# part 1
T = True
while T == True:
	inp = input()
	# if q or Q is typed quit
	if inp.lower() == 'q':
		T = False
		break
	else:
		devs=0
		inp = int(inp)
		# cnt devidable possibilites
		for x in range(1,(inp+1)):
			if inp % x == 0:
				devs += 1
			else:
				continue
		# if more than 10 yes othervice no 
		if devs >= 10:
			print('yes')
		else:
			print('no')
# ------------------------------------------------------
# part 2.1
inp = int(input())

# Finding the closest two-digit num

for x in range(10, 100):
	digits = str(x)
  # go trough stirng and sum it 
	digit_sum = sum(int(digit) for digit in digits)
	
	if digit_sum ** 2 == x:
		print(x)
		break

# -------------------------------------------------------
# part 2.2
# finding the closest three-digit num

for x in range(100, 1000):
	digits = str(x)
	# go trough stirng and sum it 
	digit_sum = sum(int(digit) for digit in digits)
	
	if digit_sum ** 3 == x:
		print(x)
		break