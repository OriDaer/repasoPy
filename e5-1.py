lista=['banana','manzana','pera','mango','mandarina','frutilla']
proceso=True
while proceso==True:
    nueva=input('ingrese una fruta nueva: ')
    if nueva=='fin'or nueva=='FIN'or nueva=='Fin':
        proceso=False
        print(lista)
        break
    lista.append(nueva)
    