# skilaverkenfi 3 (PA3)
# Friðbjörn & Sara
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

# s/[str]
# leitar af orði sem að byrjar á [str] til að vinna úr

# a/[str(word)]
# bæta við orði í skjalið

# w
# WRITE LIST TO TXT FILE


def main():
	# find TXT FILE
	try:
		inp = input()
		lstfile=openfile(inp)
	# MUNA AÐ TAKA E IÐ Í BURTU =======================================================_______________=============____________===========______
	except Exception as e:
		print('File not found!', e)

	# selection option 1
	# while loop 
	# MUNA GRACEFULL DEMURE EXIT!!!!

		# búa til selection menu
		# SPLITT THE ENTRY

		# if quit selected

			# if l selected
				# if / thing is wrong

			# if s selected
				# if / thing is wrong

			# if a selected
				# if / thing is wrong

			#  if w selected
				# if / thing is wrong
		
		# selection menu 2

# ERRORS TO HANDLE 
	# wrong num, wrong scnt inp
	# str entered in int
	# missing part of action

try: 
	main()
except Exception as e:
	print(e)