import wurfelaktion
from matplotlib import pyplot as plt

startwurfel = 7
multiplikator = 1
hasenpunkte = 0

# abbruchbedingung
# anzahl_wurfel <= 1


punktesumme = 0
punkte = []

iteration = 100000

for i in range(iteration):
	puntkewurfel = 0

	while startwurfel !=1:
		if startwurfel == 0:
			startwurfel = puntkewurfel
			puntkewurfel = 0

		wurf = wurfelaktion.wurfelaktion(startwurfel,multiplikator, puntkewurfel)
		wurf.wuerfeln()

		if wurf.gueltig():
			if wurf.alles_karotte():
				break
			wurf.ergebnis()
			multiplikator =  wurf.update_multiplikator()
			if wurf.update_hasenpunkte == 0:
				multiplikator -= 1
				hasenpunkte += 2
				puntkewurfel += 1
			else:
				hasenpunkte += wurf.update_hasenpunkte()
			startwurfel = wurf.get_anzahl_wurfel()
			puntkewurfel += wurf.get_anzahl_punktewurfel()
		else:
			hasenpunkte = 0
			break
	
	punkte.append(hasenpunkte * multiplikator)
	punktesumme += punkte[i]
	hasenpunkte = 0
	multiplikator = 1
	startwurfel = 7


mittelwert = punktesumme / iteration

print "Mittelwerte der Hasenpunkte: %s" % mittelwert
plt.hist(punkte)
plt.savefig('histogram.pdf')
# plt.show()