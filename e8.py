cant=0
cant2=0
lista=[]
proceso=True
while proceso==True:
    names=str(input('ingresa un nombre: '))
    if names=='fin'or names=='FIN'or names=='Fin':
        proceso=False
        break
    lista.append(names)
lista.sort()
if proceso==False:
    for i in lista:
        if i.startswith('e') or i.startswith('E'):
            cant+=1
        if i.startswith('a') or i.startswith('A'):
            cant2+=1
    especifico=str(input('ingresa el nombre a buscar: '))
    if especifico in lista:
        print(f'el nombre {especifico} se encuentra en la lista')
    else:
        print(f'el nombre {especifico} no se encuentra en la lista')
    print(lista)
    print('la cantidad de nombres que comienzan con e o E es: ',cant)
    print('la cantidad de nombres que comienzan con a o A es: ',cant2)
