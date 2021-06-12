
#-------Definicion de variables-----#
A = 0
B = 0
i = 1
#-------Definicion de funciones-----#
def  cachipun(jugador1,jugador2):
    if jugador1 == jugador2 :
        return  '0-0'
    if jugador1 == 'PAPEL' and jugador2 == 'PIEDRA':
        return '1-0'
    if jugador1 == 'PAPEL' and jugador2 == 'TIJERA':
        return '0-1'
    if jugador1 == 'PIEDRA' and jugador2 == 'PAPEL':
        return '0-1'
    if jugador1 == 'PIEDRA' and jugador2 == 'TIJERA':
        return '1-0'
    if jugador1 == 'TIJERA' and jugador2 == 'PAPEL':
        return '1-0'
    if jugador1 == 'TIJERA' and jugador2 == 'PIEDRA':
        return '0-1'

#-------Inicio de programa -------#


print("\n JUEGO DEL CACHIPUN\n")

while A <=2 and B <= 2 :
    
    print("Ronda #",i)
    user1= input('Cual es su jugada -jugador A: ').upper ().strip()         #SE CONVIERTE EN MAYUSCULA Y SE QUITAN LOS ESPACIOS
    user2= input('Cual es su jugada -jugador B: ').upper ().strip()

    if user1 in ('TIJERA','PIEDRA','PAPEL') and user2 in ('TIJERA','PIEDRA','PAPEL'):

        ronda = cachipun(user1,user2)                                       # SE INSERTAN LOS PARAMETROS EN LA FUNCION

        A += int(ronda[0:1])                                                # SE EXTRAE EL PRIMER CARACTER EN LA POSICION 0 HASTA LA POSICION 1
        B += int(ronda[2:3])                                                # SE EXTRAE EL TERCER CARACTER EN LA POSICION 2 HASTA LA POSICION 3

        print('A: ',user1)
        print('B: ',user2)
        print(A,'-',B,'\n')
        i += 1
        
    else:
        print('\n Por favor escriba una jugada valida \n')

if A == 3:
    print("El ganador es A")
else:
    print("El ganador es B")