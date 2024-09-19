# fribbi
# safe_division

def divide_safe(x,y):
	try:
		x = float(x)
		y = float(y)

		return round(x/y,5)
	except:
		return None
		
num1_str=input()
num2_str=input()
print(divide_safe(num1_str, num2_str))