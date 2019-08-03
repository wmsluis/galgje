import re
import random

class Galgje(object):
    """ Een spelletje galgje """

    def __init__(self, woordenlijst):
        self.woordenlijst = woordenlijst
        self.missers = []
 
    def speel(self, maxgok):
        self.max_gokken = maxgok
        self.het_woord = random.choice(self.woordenlijst).upper()
        self.invul = ['_'] * len(self.het_woord)    # array met gedeeltelijk ingevulde antwoord
        
        toestand = "toon_voortgang"
        while toestand != "exit":
            actie = getattr(self, toestand)
            toestand = actie()

    # toestandsfuncties
    def toon_voortgang(self):
        self.print_voortgang()
        if len(self.missers) >= self.max_gokken:
            return "te_veel_pogingen"

        if '_' not in self.invul:
            return "woord_geraden"
        
        return "ophalen_gok"

    def te_veel_pogingen(self):
        print(f'Jammer joh! Dat was kennelijk te moeilijk :-p  Het woord was: {self.het_woord} ')
        return "exit"

    def woord_geraden(self):
        print(f"\nGefeliciteerd, je hebt het geraden!!!'")
        return "exit"
     
    def ophalen_gok(self):
        self.gok = input("Raad een letter (of type een punt(.) om te stoppen): ").upper()
        if self.gok == ".":
            return "exit"

        if len(self.gok) != 1 or not self.gok.isalpha():
            print("\nIncorrect invoer, vul één letter in.")
            return "ophalen_gok"

        if self.gok in self.invul + self.missers:
            print("\nDeze letter is al gebruikt.")
            return "ophalen_gok" 

        if self.gok in self.het_woord:
            return "goede_gok" 
            
        return "foute_gok" 

    def goede_gok(self):
        for index, letter in enumerate(self.het_woord):
            if letter == self.gok:
                self.invul[index] = self.gok
        return "toon_voortgang"

    def foute_gok(self):
        self.missers += self.gok
        return "toon_voortgang"

    # hulpfuncties: geen toestand functies
    def invul_woord(self):
        return " ".join(self.invul)

    def invul_missers(self):
        c = self.missers + ["_"] * (self.max_gokken - len(self.missers))
        return " ".join(c)

    def print_voortgang(self):
        print(f'\nGalgje woord: {self.invul_woord()}')
        print(f'Missers: {self.invul_missers()}')

