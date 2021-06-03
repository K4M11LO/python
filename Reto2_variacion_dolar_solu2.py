n = int(input('Por favor ingrese el número de dias: '))

i = 0
mayor = 0
indice = 0
vdi = 0

while n > i:
    vd = float(input('ingrese valor del dolar ' + str(i+1)+ ': '))
    if i == 0:
       alza = 0
    else:
        alza = (vd - vdi)

    if alza >= mayor:
        mayor = alza
        indice = i + 1
    vdi = vd
    i = i+1
if alza == 0:
    print('Sin alzas')
else: 
    print('El valor del dolar mayor es: ',mayor)
