import wurfelaktion
from matplotlib import pyplot as plt

startwurfel = 7
multiplikator = 1
hasenpunkte = 0

# Einige Keywords die benötigt werden um eine Strategie zu definieren:
# 'anzahl_wurfel_abbruch' benennt die Anzahl würfel in der Hand des Würfelnden, bei der er nichtweiterwürfelt, sondern die erwürfelten Punkte nimmt
# 'multiplikatorx_abwann' bezeichnet die "Runde" in der der x-te Multiplikator rausgelegt werden darf. Dabei bezeichnet 1 sofort die allererste Runde
#  		in der man mit 7 Würfeln startet, Runde 2 die Runde, nachdem man sich das erste Mal Häschenpunkte hat festhalten lassen usw.
# 'wurfel_raus' beschreibt die Strategie nach der Häschen gewählt werden. Folgende Optionen sind möglich:
#		max: es werden immer alle möglichen Hasen rausgelegt
#		min: es wird immer die minimal mögliche anzahl an würfeln herausgelegt - sollten also zwei einerhasen und ein doppelhase gewürfelt worden sein, wird sich
# 			 für den doppelhasen entschieden, da weniger würfel benötigt werden um weiterzuwürfeln. Im falle eines doppelhasen und eines einerhasen, ebenfalls der 
#			 doppelhase, da dieser bei gleicher anzahl würfel die größere punkt zahl ergibt.
#      	minmax: Es wird darauf geachtet, dass wiederum eine möglichst kleine Anzahl würfel immer herausgelegt wird, bei allerdings möglichst maximaler Punktzahl. 
#				Im Vergleich zur Option "min" werden hier beispielsweise die beiden einzelhasen dem doppelhasen vorgezogen.
# 'abbruch_punkte' beschreibt die Mindestanzahl Punkte die in Kombination mit der "anzahl_wurfel_abbruch" bedingung ebenfalls zum nicht weiterwürfeln führt



# Strategie dicts
# Strategie im ersten Durchgang maximal den zweier Multiplikator rauslegen, danach komplett, abbruch bei einem verbleibenden Würfel
strat = ['anzahl_wurfel_abbruch': 1,
		 'abbruch_punkte': 30,
		 'multiplikator2_abwann': 1,
		 'multiplikator3_abwann': 2,
		 'multiplikator4_abwann': 2,
		 'multiplikator5_abwann': 2,
		 'wurfel_raus': 'minmax']

# abbruchbedingung
# anzahl_wurfel <= 1


punktesumme = 0
punkte = []

iteration = 100000

for i in range(iteration):
	puntkewurfel = 0

	while startwurfel !=strat['anzahl_wurfel_abbruch'] or hasenpunkte * multiplikator >= strat['abbruch_punkte']:
		if startwurfel == 0:
			startwurfel = puntkewurfel
			puntkewurfel = 0

		wurf = wurfelaktion.wurfelaktion(startwurfel,multiplikator, puntkewurfel, strat)
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