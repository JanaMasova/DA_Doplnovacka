
def doplnovacka(vstup, num):
	seznam = []
	text = ""
	if ".txt" in vstup or ".html" in vstup:
		with open (vstup) as f:
			text = f.read()
		f.closed
	else:
		text = vstup
	

	text = text.replace("\n","*")
	vysledek = []
	seznam = text.split()
	interpunkce = ".,?!:/'\""


	for i in range(0,len(seznam)):
		slovo = seznam[i]
		slovoUpraveno = ""
		if (i + 1) % num == 0:
			for pismenko in slovo:
				if pismenko not in interpunkce:
					slovoUpraveno += "-"
				else:
					slovoUpraveno += pismenko
			vysledek.append(slovoUpraveno)
		else:
			vysledek.append(slovo)

	s = " ".join(vysledek)
	s = s.replace("*","\n")
	print(s)

doplnovacka(
vstup = input("Zadej text nebo soubor ve formátu txt. nebo .html, který chceš nahradit: "),
num = int(input("Zadej, kolikátá slova chceš nahradit: ")))
