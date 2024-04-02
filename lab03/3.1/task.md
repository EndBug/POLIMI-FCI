# Esercizio 3.1

Si vuole scrivere un'applicazione client/server TCP per conteggiare il numero di consonanti presenti in una stringa.

- Il client chiede all'utente di inserire una stringa.
- Il server risponde indicando il numero di consonanti presenti nella stringa (sia maiuscole che minuscole).

_Hint: `y.count(x)` conta quante volte appare l’elemento `x` nella lista `y`._

Scrivere gli script "TCP client" e "TCP server" date le seguenti specifiche:
- Utilizzare indirizzi IPv4
- Time out in ricezione (lato client): 2 secondi
- Lunghezza buffer di ricezione: 2048 byte