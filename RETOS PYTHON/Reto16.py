miLista = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]



'''

if len(miLista[0]):
    print("no vacio")
else:
    print("vacio")
    miLista.pop(0)
    print(miLista)


if len(miLista[1]):
    print("no vacio")
else:
    print("vacio")
    miLista.pop(1)
    print(miLista)
'''

for i in miLista:
    if len(miLista[i]):
        print("no vacio")
    else:
        print("vacio")
        miLista.pop(i)
        print(miLista)