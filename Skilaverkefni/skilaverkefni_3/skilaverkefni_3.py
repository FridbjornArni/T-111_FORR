# skilaverkenfi 3 (PA3)
# Friðbjörn
# 7.10.24

# read in txt line by line
# skila lista
def openfile(skjal):
	lstfile = []
	with open(skjal) as F:
		lstfile = F.read().strip().split('\n')
	return lstfile

# l/[eitthver tala]
# print out line nr eih 
def linereader(x,lst):
	if len(lst)< x or x<0:
		return "Invalid line number!"
	else:
		return lst[x]



# s/[str]
# leitar af orði sem að byrjar á [str] til að vinna úr

# a/[str(word)]
# bæta við orði í skjalið
def addtofile(x,lst):
	return lst.append(x)
	

# w
# WRITE LIST TO TXT FILE
def writetofile(lst,skjal):
	try:
		with open(skjal) as F:
			F.write(lst)
		return 'File written!'
	except:
		pass

def main():
	run = True
	# find TXT FILE
	try:
		inp = input()
		lstfile=openfile(inp)
	# MUNA AÐ TAKA E IÐ Í BURTU =======================================================_______________=============____________===========______
	except Exception as e:
		print('File not found!', e)
	print(lstfile)
	# selection option 1
	# while loop 
	# MUNA GRACEFULL DEMURE EXIT!!!!
	# búa til selection menu
	print('l/<line>: prentalínu\ns/<search_string>: leitar í filenum\na/<new word>: bætir við orði\nw: skrifar í skrá\nq: hætta')
	inp=input()
	# SPLITT THE ENTRY
	try:
		inp, inp2 = inp.split('/')
	except:
		pass

	while run == True:
		# if quit selected
		if inp.lower() == 'q':
			run = False
		else:
			# if l selected
			if inp.lower() == 'l':
				# if / thing is wrong
				try:
					print(linereader(int(inp2)-1,lstfile))
				except Exception as e:
					print(e)

			# if s selected
			elif inp.lower() == 's':
				# if / thing is wrong
				try:
					pass
				except:
					continue
				pass

			# if a selected
			elif inp.lower() == 'a':
				# if / thing is wrong
				try:
					lstfile = addtofile(inp2,lstfile)
				except:
					continue

			#  if w selected
			elif inp.lower() == 'w':
				# if / thing is wrong
				try:
					pass
				except:
					continue 
				pass
			else:
				print('eitthvað hefur misheppnast')
		
		# selection menu 2
			print('l/<line>: prentalínu\ns/<search_string>: leitar í filenum\na/<new word>: bætir við orði\nw: skrifar í skrá\nq: hætta')
			inp=input()
			# SPLITT THE ENTRY
			try:
				inp, inp2 = inp.split('/')
			except:
				continue
# ERRORS TO HANDLE 
	# wrong num, wrong scnt inp
	# str entered in int
	# missing part of action

try: 
	main()
except Exception as e:
	print(e)