# RETO 4 - JUAN CAMILO ROCHA - COINCIDENCIA DNA


#DEFINICION DE FUNCIONES

def coincidencia (p):
    
    contador = 0
    total = 0
    
    tupla = [('Pedro', '00000101010101010101'),
            ('Juan' ,  '00101010101101110111'),
            ('Diego',  '00100010010000001001')       
    ]
    
    #lista1 = ['Pedro','Juan','Diego']
    #lista2 = ['00000101010101010101','00101010101101110111','00100010010000001001']

    for i in range  (len(tupla)) :     #(len(lista2)) :     #usar con listas
            dna = list(tupla[i][1])    #list(lista2[i])     #usar con listas 
            nombre = tupla[i][0]      #lista1[i]            #usar con listas 
            #print('\n')

            for n in range (len(dna)):            
                valor1 = dna[n]
                valor2 = p[n]                

                if valor1 == valor2:
                   contador += 1
                #print(valor1,valor2,contador)
                

            if contador > total:
                total = contador
                nombreCulp = nombre
                contador = 0
            else:
                contador = 0
            #print(total,nombreCulp)
    print( 'El culpable es ',nombreCulp,' con un parentezco de ' , total*(100/20),'%')            

#DEFINICON DE VARIABLES
error = 0


# INICIO DE PROGRAMA
print('\t COINCIDENCIA DNA')
cromosoma = list(input('Por favor ingrese el cromosoma: '))
                                                                    
for  j in range (len(cromosoma)) :                                  #Verifica que los numeros estén entre 0 y 1 
    
    if 0 <= int(cromosoma[j]) <= 1:
        None
    else:    
        error += 1

if error > 0 :
    print('Inserte numeros validos entre 0 y 1')      
else:
                                                                    
    if len(cromosoma) == 20 :                                       #Verifica que la longitud del cromosoma sea de 20
        
        coincidencia(cromosoma)

    else:
        print('Longitud de cromosoma invalido',len(cromosoma),'/20')

input()    
