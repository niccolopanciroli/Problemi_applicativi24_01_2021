print("Risolvi il problema precedente partendo da due liste che generano un dizionario con lazione come chiave e la capitale come valore. Successivamete interroga il dizionario per visualizzare la capitale di una nazione")
input()

nazioni = ["Italia", "Francia", "Spagna", "Inghilterra", "Germania", "Svizzera", "Polonia"]
capitali = ["Roma", "Parigi", "Madrid", "Londra", "Berlino", "Berna", "Varsavia"]

nazioni_capitali = {}

for n, c in zip(nazioni, capitali):
    nazioni_capitali[n] = c

print(nazioni_capitali)
print()

stato = str(input("Inserisci la nazione della quale vuoi conoscere la capitale "))
if stato not in nazioni_capitali:
    print("Il programma non conosce questa nazione")
    print("Le nazioni che conosco sono:", nazioni)
else:
    print(nazioni_capitali[stato])
