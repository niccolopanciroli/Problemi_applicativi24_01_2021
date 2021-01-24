print("Costruisci un dizionario ottenuto da quello dell'esercizio precedente invertendo il ruolo di chiave e valore. Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale")
print()

nazioni = ["Italia", "Francia", "Spagna", "Inghilterra", "Germania", "Svizzera", "Polonia"]
capitali = ["Roma", "Parigi", "Madrid", "Londra", "Berlino", "Berna", "Varsavia"]

nazioni_capitali = {}

for n, c in zip(nazioni, capitali):
    nazioni_capitali[c] = n

print(nazioni_capitali)

capitale = input("Scegli una capitale: ")
if capitale in nazioni_capitali:
    nazione = nazioni_capitali[capitale]
    print(capitale, "è capitale della nazione", nazione)
else:
    print("Il programma non conosce la nazione associata alla capitale ", capitale)