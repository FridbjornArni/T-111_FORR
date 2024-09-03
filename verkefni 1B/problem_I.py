A=int(input())
B=int(input())

if A >= 350 or B >= 350:
	print('shutdown')
elif A > B and (A > 300 or B > 300):
	print('keep')
elif A < B and (A > 300 or B > 300):
	print('keep')
elif A == B and (A > 300 or B > 300):
	print('lower')
elif A == B and A == 300:
	print ('keep')
elif A > B and (A < 300 or B < 300):
	print('keep')
elif A < B and (A < 300 or B < 300):
	print('raise')
elif A == B and (A < 300 or B < 300):
	print('raise')