lista=['banana','manzana','pera','mango','mandarina','frutilla']
especifico=str(input('ingresa una fruta a buscar: '))
if especifico in lista:
    print(f'la fruta {especifico} se encuentra en la lista')
else:
    print(f'la fruta {especifico} no se encuentra en la lista')