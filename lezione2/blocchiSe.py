# Nella scorsa lezione abbiamo visto i blocchi if e else.
# Per usarli implicitamente abbiamo fatto uso di valori booleani.

a = int(input("Inserisci il primo valore: "))
b = int(input("Inserisci il secondo valore: "))
c = int(input("Inserisci il terzo valore: "))

if a > b:
    if a > c:
        massimo = a
        if b > c: 
            minimo = c
        else:
            minimo = b
    else:
        massimo = c
        minimo = b
else:
    if b > c:
        massimo = b
        if a > c:
            minimo = c
        else:
            minimo = a
    else:
        massimo = c
        minimo = a

print("Il valore massimo è: ", massimo)
print("Il valore minimo è: ", minimo)

input()

#! elif blocco corrispondente all'else if. Permette di eseguire un blocco di codice
#! solo se la condizione precedente è falsa, e la condizione corrente è vera.
# ora vediamo una semplificazione dell'esercizio precedente
# usando i blocchi elif

a = int(input("Inserisci il primo valore: "))
b = int(input("Inserisci il secondo valore: "))
c = int(input("Inserisci il terzo valore: "))

if a > b and a > c:
    massimo = a
    if b > c:
        minimo = c
    else:
        minimo = b
elif b > c:
    massimo = b
    if a > c:
        minimo = c
    else:
        minimo = a
else:
    massimo = c
    if b < a:
        minimo = b
    else:
        minimo = a

print("Il valore massimo è: ", massimo)
print("Il valore minimo è: ", minimo)

input()

#! Python è un linguaggio molto potente e comprende da solo molte funzioni utili.
#! Tra queste sono presenti le funzioni max e min

massimo = max(a, b, c)
minimo = min(a, b, c)

print("Il valore massimo è: ", massimo)
print("Il valore minimo è: ", minimo)