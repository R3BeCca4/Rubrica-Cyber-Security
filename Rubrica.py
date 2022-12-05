# Il progetto si basa sulla realizzazione di una "rubrica" contenente una lista di nomi

# Le funzionalità da implementare sono le seguenti:
# Aggiungi nome, modifica nome, elimina nome, visualizza tutti i nomi, esci dal programma.


def aggiungi_nome(lista, nome):
    return

def modifica_nome(lista, vecchio, nuovo):
    indice = -1
    i = 0
    while i < len(lista):
        if lista[i] == vecchio:
            indice = i
            break
    lista[indice] = nuovo
    return lista

def rimuovi_nome(lista, nome):
    nuova_lista = []
    for n in lista:
        if n != nome:
            nuova_lista.append(n)
    return nuova_lista

def stampa_lista(lista):
    return


print("Benvenuto nella ribrica")
print("Comandi disponibili: aggiungi, modifica, rimuovi, lista, esci")

comando = input("inserisci comando >> ")

lista_nomi = []
termina = False

while not termina:
    match comando:
        case 'aggiungi':
            nuovo_nome = input("Inserisci nome da aggiungere >> ")
            lista_nomi = aggiungi_nome(lista_nomi, nuovo_nome)
        case 'modifica':
            vecchio_nome = input("Inserisci quale nome modificare >> ")
            nuovo_nome = input("Inserisci il nuovo nome da dargli >> ")
            lista_nomi = modifica_nome(lista_nomi, vecchio_nome, nuovo_nome)
        case 'rimuovi':
            nome = input("inserisci nome da rimuovere >> ")
            lista_nomi = rimuovi_nome(lista_nomi, nome)
        case 'lista':
            stampa_lista(lista_nomi)
        case 'esci':
            termina = True
        case _:
            print("hai inserito un comando sbagliato, riprova")
    
    if not termina:
        comando = input("inserisci comando >> ")

print("Programma terminato.")