num=int(input('ingrese un num entero: '))
suma=0
while(num>=0):
    suma+=num
    print(suma)
    num=int(input('ingrese un num entero: '))
if (num<0):
    print('la suma de los numeros ingresados es:', suma) 