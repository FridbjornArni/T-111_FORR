import random
# tryer = 0
# tal = random.randint(0,1000)
# while tryer < 10:
# 	tryer += 1
# 	inp = int(input())

# 	if inp == tal:
# 		print("correct")
# 		break
# 	elif tal > inp:
# 		print("higher", flush=True)
# 	elif tal < inp:
# 		print("lower", flush=True)
	

x=1000
y=0
guess = 0
while True:
	guess = random.randint(y,x)
	cmd = input()
	if "correct" == cmd or "c" == cmd:
		break
	elif "higher" == cmd or "h" == cmd:
		y = guess
	elif "lower" == cmd or "l" == cmd:
		x = guess
	