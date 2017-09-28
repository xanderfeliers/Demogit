naam = "Feliers"
voornaam = "Xander"
email = "xander.feliers@student.howest.be"

print (naam)
print (voornaam)
print (email)

print("Labo Basic Programming,\n\tLabo week 1\n\t\tKennismaking met  Python,\n\t\tWerken met variabelen.\nLabo Basic Programming,\n\tLabo week 2")

#basis = input ("geef de basis") basis is van het type string => can't multiply
#met float () kan je een string of int omzetten naar een type float
basis = float(input("Geef de basis van de driehoek op: "))
hoogte = input("Geef de hoogte van de driehoek op: ")
hoogte = float(hoogte)
opp_driehoek = basis * hoogte / 2
print("De oppervlakte bedraagt {0}".format(opp_driehoek))

aantal_dagen= int (input("Geef het aantal dagen op: "))
aantal_uren= int (input("Geef het aantal uren op: "))
aantal_minuten= int (input("Geef het aantal minuten op: "))
aantal_seconden= int (input("Geef het aantal seconden op: "))
totaal = aantal_seconden + 60 * aantal_minuten + aantal_uren * 60 * 60 + aantal_dagen *24 *60 *60
print("Het totale aantal seconden bedraagt {0}".format(totaal))


tijd = float(input("Geef het aantal seconden op: "))
dag = tijd // (24 * 3600)
tijd = tijd % (24 * 3600)
uur = tijd // 3600
tijd %= 3600
minuten = tijd // 60
tijd %= 60
seconden = tijd
print("d:h:m:s-> %d:%d:%d:%d" % (dag, uur, minuten, seconden))



n=input("Geef een getal n: ")
som=(int(n*1)) + (int(n*2)) + (int(n*3))
print("Het resultaat is {0}".format(som))

x=float (input("Geef een getal op: "))
y=float (input("Geef een getal op: "))
formule=(x+y)*(x+y)
print("(%d + %d) ^ 2 = %d" % (x,y,formule))