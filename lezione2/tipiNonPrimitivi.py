# In python esistono anche dei tipi non primitivi.

#! I tipi non primitivi sono:
#? - list	-> lista
#? - tuple	-> tupla
#? - set	-> set
#? - dict	-> dizionario
#? - NoneType	-> None

# Iniziamo dalla lista
# Una lista è una sequenza di elementi di qualsiasi tipo
lista = [1, 3.0, "Ciao", True]

#Possiamo stampare la lista con print
print("lista:", lista, "è di tipo", type(lista))

# Ora creiamo una lista vuota
lista = []

# Possiamo aggiungere elementi alla lista con il metodo append
lista.append(1)
lista.append(2)
lista.append(3)

print("lista:", lista)

# Possiamo accedere agli elementi della lista con gli indici
print("lista[0]:", lista[0])

# Possiamo inoltre accedere e modificare gli elementi della lista con gli indici
lista[0] = 4
print("lista[0]:", lista[0])
print("lista:", lista)
