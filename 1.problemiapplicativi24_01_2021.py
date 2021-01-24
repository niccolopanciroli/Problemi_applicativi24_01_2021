print("Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali (nazione e relativa capitale si trovano nella medesima posizione delle rispettive liste), visualizza la capitale di una nazione della quale viene fornito da tastiera il nome, segnalando con un messaggio di errore il caso in cui la nazione richiesta non sia compresa nell'elenco")

input()

nazioni = ["Italia", "Francia", "Spagna", "Inghilterra", "Germania", "Svizzera", "Polonia"]
capitali = ["Roma", "Parigi", "Madrid", "Londra", "Berlino", "Berna", "Varsavia"]

def main():
    domanda = str(input("Inserisci la nazione della quale vuoi conoscere la capitale "))

    if domanda in nazioni:
        n = nazioni.index(domanda.capitalize())
        c = capitali[n]
        print("La capitale della nazione scelta: ", domanda," è: ", c)
    else:
        print("Questo programma non comprende la nazione scelta")
main()