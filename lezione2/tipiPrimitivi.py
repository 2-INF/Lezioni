# prendiamo in input due variabili a e b

a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero:")

# e stampiamo il loro tipo

print("a:", a, "è di tipo", type(a))
print("b:", b, "è di tipo", type(b))

# Quando usiamo la funzione input viene "restituito" un valore di tipo stringa
# Questo tipo è detto primitivo.
# 
#! In python esistono un totale di 4 tipi primitivi:
#? - int     -> interi
#? - float   -> numeri con la virgola
#? - str    	-> stringhe
#? - bool	-> booleani

input()

# Se proviamo ad eseguire una somma dei due valori...
somma = a + b
print("La somma è:", somma)
# ... otteniamo un risultato sbagliato.
#
# Per ottenere il risultato corretto della somma dobbiamo convertire i valori
# nel tipo che desideriamo.

input()

# Convertiamo a e b in interi
a_int = int(a)
b_int = int(b)
print("a:", a_int, "è di tipo", type(a_int))
print("b:", b_int, "è di tipo", type(b_int))
# Notiamo che ora il loro tipo è cambiato in un tipo intero

input()

# Eseguendo la somma otteniamo il risultato corretto
somma = a_int + b_int
print("La somma è:", somma)
input()

#! Se proviamo ad inserire dei valori non interi otteniamo un errore

# Chiediamo nuovamente a e b
a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero:")

# Convertiamo a e b in numeri con la virgola
a_float = float(a)
b_float = float(b)

print("a:", a_float, "è di tipo", type(a_float))
print("b:", b_float, "è di tipo", type(b_float))

# Eseguendo la somma otteniamo il risultato corretto
somma = a_float + b_float
print("La somma è:", somma)

input()

# L'ultimo tipo primitivo è il booleano
# Un booleano può assumere solo due valori: True o False
a = input("Inserisci il primo valore: ")
b = input("Inserisci il secondo valore:")
# Convertiamo a e b in booleani
a_bool = bool(a)
b_bool = bool(b)

print("a:", a_bool, "è di tipo", type(a_bool))
print("b:", b_bool, "è di tipo", type(b_bool))

input()

# Le variabili booleane vengono utilizzate per eseguire operazioni di confronto
# tra due valori
# Vediamo alcuni esempi
print("3 > 2?", 3 > 2)
input()

print("3 < 2?", 3 < 2)
input()

print("3 == 2?", 3 == 2)
input()

print("3 != 2?", 3 != 2)
input()

print("3 >= 2?", 3 >= 2)
input()

print("3 <= 2?", 3 <= 2)
input()

# I valori booleani posseggono inoltre delle operazioni proprie
# Vediamo alcuni esempi
print("True and True?", True and True)
input()

print("True and False?", True and False)
input()

print("True or True?", True or True)
input()

print("True or False?", True or False)
input()

print("not True?", not True)
input()

print("not False?", not False)
# ecc...
