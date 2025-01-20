# Fribbi
# 18.10.24
# Skilaverkefni 4 (PA4)

class skil4:
	def __init__(self,file1) -> None:
		self.file1 = file1
		pass
	
	def show_const():
		pass
		return 1

	def show_party():
		return 1

	def show_results():
		return 1

	def maklstnorm1():
		# Breidd dálkanna tveggja er 20 fyrir ‘Constituency’ og 10 fyrir ‘Electorals’.
		pass

	def maklstnorm2():
		# Breidd dálkanna tveggja er 6 fyrir ‘List‘ og 26 fyrir ‘Party’
		pass

	def maklstnorm3():
# 	Breidd dálkanna fjögurra eru 10, 26, 10 og 10 fyrir ‘List‘, ‘Party‘, ‘Votes’ og ‘Ratio’, í sömu röð. Gildið fyrir dálkinn ’Ratio’ ætti að vera sniðið þannig að það hafi einn tölustaf á eftir aukastafnum. Gildi dálksins ‘Turnout’ er reiknað sem hlutfall heildaratkvæða af fjölda kosningabærra manna í viðkomandi kjördæmi.
		pass



def selection():
	print('1. Show constituencies\n2. Show parties\n3. Show results\n9. Quit')
	return input()


def main():
	inp = selection()
	while inp!='9':
		try:
			if inp == '1':
				try:
					fileName = input()
					skil4
					show_const()
				except:
					print('wrong file name')
			elif inp == '2':
				show_party()
			elif inp == '3':
				show_results()
			inp = selection()
		except Exception as e:
			print(e)
main()

# constit.txt
# eparties.txt
# results.txt