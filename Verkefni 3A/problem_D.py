import math
sum1 = 0
sum2 = 0
cnt = 0
x = 0
avg = 0
x = float(input())
while x >= 0:
		cnt += 1
		sum1 += x
		sum2 += x**2
		avg = sum1/cnt
		devi= math.sqrt((cnt*sum2-sum1**2))/cnt
		print(f"{avg:.2f}")
		print(f"{devi:.2f}")
		x = float(input())
	