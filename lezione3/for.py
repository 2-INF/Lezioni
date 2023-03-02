# Esercizio 1
# Contare i numeri da 1 a 10

indice = 1
while indice <= 10:
    print(indice)
    indice = indice + 1

# Esercizio 2
# Per ogni numero da 1 a 10, stampare il suo quadrato

indice = 1
while indice <= 10:
    print(indice * indice)
    indice = indice + 1

#! Possiamo risparmiare righe di codice?
# Si! Usando l'operatore for possiamo risparmiare due righe di codice

# ciclo for:
#? for <variabile> in <sequenza>:

# Esercizio 1.1
# Contare i numeri da 1 a 10

for indice in range(1, 11):
    print(indice)

#! usiamo range per definire l'intervallo di numeri (o meglio indici) su cui eseguire il ciclo for

# Esercizio 2.1
# Per ogni numero da 1 a 10, stampare il suo quadrato

for indice in range(1, 11):
    print(indice * indice)

# Esercizio 3
# Scrivere un programma che chieda all'utente di inserire un numero intero e stampi
# la sua tabellina (da 1 a 10)



# Esercizio 4
# Scrivere un programma che chieda all'utente di inserire un numero intero e stampi
# la tabellina di quel numero (da 1 a 10) solo se il numero è minore di 10 e maggiore di 0



# Esercizio 5
# Scrivere un programma che chieda all'utente di inserire un numero intero e stampi
# la sequenza di Fibonacci fino a quel numero



# Esercizio 6
# Scrivere un programma che chieda all'utente di inserire un numero intero e stampi
# se il numero è primo o no
