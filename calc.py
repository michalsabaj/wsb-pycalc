def suma(x, y):
	return x+y
def roznica(x, y):
	return x-y
def iloczyn(x, y):
	return x*y
def iloraz(x, y):
	return x/y

while True:
	print("Kalkulator")
	print("0 - suma")
	print("1 - roznica")
	print("2 - iloczyn")
	print("3 - iloraz")
	print("4 - wyjdz")

	opcja = input("Wybierz opcje: ")
	if opcja == '4':
		print("koniec")
		break

	if opcja in ('0', '1', '2', '3', '4'):
		x = float(input("pierwsza liczba: "))
		y = float(input("druga liczba: "))
		if opcja == '0':
			print(x, "+", y, "=", suma(x,y))
		elif opcja == '1':
			print(x, "-", y,"=", roznica(x,y))
		elif opcja == '2':
			print(x, "*", y,"=", iloczyn(x,y))
		elif opcja == '3':
			if y != 0:
				print(x, "/", y,"=", iloraz(x,y))
			else:
				print("Nie dziel przez 0")
	else:
		print("blad, zla opcja")
