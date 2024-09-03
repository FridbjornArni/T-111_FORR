l1 = input()
l2 = input()
l3 = input()
l4 = input()
k1=''
q=0
cnt = 0
for x in l1:
	if q == 0:
		q+=1
		y = ord(x)
		while chr(y) != 'H':
			if y != ord('H'):
				if y < ord('H'):
					y+=1
					cnt += 1
				elif y > ord('H'):
					y-=1
					cnt -=1 
	else:
		break
for x in [l1, l2, l3, l4]:
	for r in x:
		r = ord(r) + cnt
		if r >= 127:
			r -=95
			k1 += chr(r)
		elif r <= 31:
			r+=95
			k1 += chr(r)
		else:
			k1 += chr(r)
	print(k1)
	k1 = ''
