from __future__ import division
import numpy 

# die klasse kann ein dictionary bekommen, dass die folgenden keywords haben sein sollte
# 'anzahl_wurfel_abbruch' benennt die Anzahl würfel in der Hand des Würfelnden, bei der er nichtweiterwürfelt, sondern die erwürfelten Punkte nimmt
# 'multiplikatorx_abwann' bezeichnet die "Runde" in der der x-te Multiplikator rausgelegt werden darf. Dabei bezeichnet 1 sofort die allererste Runde
#       in der man mit 7 Würfeln startet, Runde 2 die Runde, nachdem man sich das erste Mal Häschenpunkte hat festhalten lassen usw.
# 'wurfel_raus' beschreibt die Strategie nach der Häschen gewählt werden. Folgende Optionen sind möglich:
#       max: es werden immer alle möglichen Hasen rausgelegt
#       min: es wird immer die minimal mögliche anzahl an würfeln herausgelegt - sollten also zwei einerhasen und ein doppelhase gewürfelt worden sein, wird sich
#            für den doppelhasen entschieden, da weniger würfel benötigt werden um weiterzuwürfeln. Im falle eines doppelhasen und eines einerhasen, ebenfalls der 
#            doppelhase, da dieser bei gleicher anzahl würfel die größere punkt zahl ergibt.
#       minmax: Es wird darauf geachtet, dass wiederum eine möglichst kleine Anzahl würfel immer herausgelegt wird, bei allerdings möglichst maximaler Punktzahl. 
#               Im Vergleich zur Option "min" werden hier beispielsweise die beiden einzelhasen dem doppelhasen vorgezogen.
# 'abbruch_punkte' beschreibt die Mindestanzahl Punkte die in Kombination mit der "anzahl_wurfel_abbruch" bedingung ebenfalls zum nicht weiterwürfeln führt

class wurfelaktion():

    def __init__(self,anzahl_wurfel,multiplikator,punktewurfel,dictio):
        self.anzahl_wurfel = anzahl_wurfel
        self.multiplikator = multiplikator
        self.anzahl_punktewurfel = punktewurfel
        self.strategy = dictio

    def anzahl_in_array(self,string):
        anzahl = 0
        for i in self.wuerfel:
            # print i
            if i == string:
                anzahl += 1
        # print anzahl  
        return anzahl

    def wuerfeln(self):
        self.wuerfel = []
        for i in range (self.anzahl_wurfel):
            zahl = numpy.random.random()
            if zahl < 1/6:
                self.wuerfel.append("karotte")
            elif zahl > 1/6 and zahl < 1/3:
                self.wuerfel.append("hase")
            elif zahl > 1/3 and zahl < 1/2:
                self.wuerfel.append("doppelhase")
            elif zahl > 1/2 and zahl < 2/3:
                self.wuerfel.append("dreifachhaus")
            elif zahl > 2/3 and zahl < 5/6:
                self.wuerfel.append("vierfachhaus")
            else:
                self.wuerfel.append("fuenffachhaus")
        # print self.wuerfel

    def alles_karotte(self):
        bool_wert = True
        for x in self.wuerfel:
            if x != "karotte":
                bool_wert = False
                break
        return bool_wert

    def gueltig(self):
        return ("hase" in self.wuerfel or "doppelhase" in self.wuerfel) or (self.alles_karotte())


    def ergebnis(self):
        self.anzahl_hasen = self.anzahl_in_array("hase")
        self.anzahl_doppelhasen = self.anzahl_in_array("doppelhase")
        self.anzahl_dreifachhaus = self.anzahl_in_array("dreifachhaus")
        self.anzahl_vierfachhaus = self.anzahl_in_array("vierfachhaus")
        self.anzahl_fuenffachhaus = self.anzahl_in_array("fuenffachhaus")
        self.anzahl_karotte = self.anzahl_in_array("karotte")

    def update_hasenpunkte(self):
        hasenpunkte =  2*self.anzahl_doppelhasen + int(self.anzahl_hasen/2)*10 + self.anzahl_hasen%2
        self.anzahl_wurfel -= (self.anzahl_doppelhasen + self.anzahl_hasen)
        self.anzahl_punktewurfel = (self.anzahl_doppelhasen + self.anzahl_hasen)
        return hasenpunkte

    def update_multiplikator(self):
        if self.multiplikator == 4:
            if "fuenffachhaus" in self.wuerfel:
                self.multiplikator = 5
                self.anzahl_wurfel -= 1
        if self.multiplikator == 3:
            if "vierfachhaus" in self.wuerfel:
                self.multiplikator = 4
                self.anzahl_wurfel -= 1
        if self.multiplikator == 2:
            if "dreifachhaus" in self.wuerfel:
                self.multiplikator = 3
                self.anzahl_wurfel -= 1
        if self.multiplikator == 1:
            if ("doppelhase" in self.wuerfel and "hase" in self.wuerfel) or (self.wuerfel.count("doppelhase") > 1):
                self.multiplikator = 2
                self.anzahl_doppelhasen -= 1
                self.anzahl_wurfel -= 1

        return self.multiplikator

    def get_anzahl_wurfel(self):
        return self.anzahl_wurfel

    def get_anzahl_punktewurfel(self):
        return self.anzahl_punktewurfel

