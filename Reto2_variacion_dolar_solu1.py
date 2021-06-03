"""    JUAN CAMILO ROCHA CAICEDO 27/05/2021
RETO 2
Escriba un programa que pida al usuario ingresar el número n de días, y luego el precio del dólar para cada uno de los n días.
El programa debe entregar como salida cuál fue la mayor de las alzas de un día para el otro.
Si en ningún día el precio subió, la salida debe decir: No hubo alzas.
"""

print ('   \n  VARIACION DIARIA DEL PRECIO DEL DOLAR \n')
dias_v = int(input('Por favor inserte numero de dias: '))

if dias_v > 1 :                                      # debe ingresar por lo menos dos dias 
    for i in range ( dias_v):
        print ('Valor del dia',i+1, end="")            
        
        if i == 0:                                  #valor del dia 1
            val_old = float(input(': ') )
        
        elif i >= 1:                                # Valores de los demas dias
            val_new = float(input(': ') )
            resultado_new =   val_new - val_old     #operacion matematica para ver la diferencia
            val_old = val_new                       # se reemplaza la variable temporal
            
            if i == 1: 
                resultado_old = resultado_new       #se asigna el primer resultado a una variable temporal
            else:
            
                if resultado_new > resultado_old:   # Se compara los demas resultados contra el mayor
                    resultado_old = resultado_new   # se asigna a la variable temporal el resultado

    if resultado_old == 0:
        print ("No hubo alzas.")
    else :
        print("la mayor alza fue de: ", round(resultado_old,2), " pesos.")
    input("")           
else:
    print('ERROR# Debe ingresar por lo menos dos días.')        

input("")           
        
   

    


        