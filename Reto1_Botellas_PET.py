#Reto 1 UNAB 
import time

#usuario 1
print('Usuario1')
men1lt1 = int(raw_input('Ingrese cantidad de botellas menor a un litro: ' ))   #captura la informacion de entrada (raw_input) , convierte la cadena a entero para poder hacer operaciones matematicas (int) y la asigna a una variable  =men1lt1
may1lt1 = int(raw_input('Ingrese cantidad de botellas mayores a un litro: ' )) #captura la informacion de entrada (raw_input) , convierte la cadena a entero para poder hacer operaciones matematicas (int) y la asigna a una variable  =may1lt1

suma1 = (men1lt1*100) + (may1lt1*150)										   #realiza una operacion matematica y la asigna a una variable suma1
print ('Valor a pagar: ' + str(suma1)  + ' pesos.')							   #imprime una cadena y le concatena el resultado de la operacion
print('')																	   # para concatenar se puede usar , o + 
																			   
#usuario 2
print('Usuario2')
men1lt2 = int(raw_input('Ingrese cantidad de botellas menor a un litro: ' ))   
may1lt2 = int(raw_input('Ingrese cantidad de botellas mayores a un litro: ' )) 

suma2 = (men1lt2*100) + (may1lt2*150)											
print 'Valor a pagar: ' , suma2  , ' pesos.'        						    # cuando se usa + para concatenar hay que tener en cuenta que todos los datos deben tener el mismo tipo
print('')																		# en este caso se utiliza str para convertir de numero a cadena (opcional)

#usuario 3
print('Usuario3')
men1lt3 = int(raw_input('Ingrese cantidad de botellas menor a un litro: ' ))    
may1lt3 = int(raw_input('Ingrese cantidad de botellas mayores a un litro: ' ))  

suma3 = (men1lt3*100) + (may1lt3*150)											
print ('Valor a pagar: ' + str(suma3) + ' pesos.')                              
print('')


#Total y promedio de botellas menor de un litro.
print('Totales y Promedios')
totalmen1lt = men1lt1+men1lt2+men1lt3												#operacion matematica para sacar el total 
prommen1lt = totalmen1lt/3 												            #operacion matematica para sacar el promedio
print ('Total botellas menor de un litro: ' + str(totalmen1lt) + ' Und.' )			# imprime el total
print('Promedio botellas menor de un litro: ' + str(prommen1lt)  + ' Und.') 		# imprime el promedio
#concatenar con + para que aparezca sin parentesis, comas y comillas

#Total y promedio de botellas mayor de un litro.
totalmay1lt = may1lt1+may1lt2+may1lt3
prommay1lt = totalmay1lt/3 

print ('Total botellas mayor de un litro: ' + str(totalmay1lt) + ' Und.'  )
print('Promedio botellas mayor de un litro: ' + str(prommay1lt) + ' Und.' )

# Total y promedio del monto pagado.
totalmon = suma1 + suma2 + suma3 
prommon = totalmon /3

print ('Total monto pagado: ' + str(totalmon) + ' pesos.')
print('Promedio monto pagado: ' + str(prommon) + ' pesos.')

time.sleep (30)   # sleep for 30 seconds
#raw_input()