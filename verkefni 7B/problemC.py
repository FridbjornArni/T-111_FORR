# Fribbi

def entries():
	x = input()
	lst = x.strip().split(' ')
	lst = [int (z) for z in lst]
	return lst

def main():
	lst = entries()
	print(lst)
	evn = [z for z in lst if z % 2 == 0]
	odd = [y for y in lst if y % 2 == 1]
	print(lst)
	print(evn)
	print(odd)

main()
