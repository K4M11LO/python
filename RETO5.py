#SISTEMA DE GESTION DE MATRICULAS JUAN CAMILO ROCHA - RETO 5 - 27/06/2021 - K4M1

import json
#Variables globales
datos_estudiantes={}
datos_estudiantes['Estudiantes']=[]

datos_docentes={}
datos_docentes['Docentes']=[]

datos_matricula={}
datos_matricula['Matriculas']=[]

datos_cursos = {}
datos_cursos['Cursos']=[]

curso1 = {'Id_curso': '1001', 'nombreCurso':'Calculo I' ,'descripcion':'Un poco de logica matematica: implicacion, negacion, cuantificadores'}
curso2 = {'Id_curso': '1002', 'nombreCurso':'Fundamentos programacion' ,'descripcion':'Es una asignatura basica para crear programas...'}
datos_cursos['Cursos'].append(curso1)
datos_cursos['Cursos'].append(curso2)

#Menu principal
def menu_principal() :
   print("___MENU PRINCIPAL_____") 
   print("___1. Docente_________") 
   print("___2. Estudiante______") 
   print("___3. Matriculas______") 
   print("___4. Reportes________") 
   print("___5. Salir___________")
   op=int(input())
   return op
#Submenu docentes
def menu_docentes() :
    print("..............................") 
    print("___MENU DOCENTES____________") 
    print("___1. Crear Docente_________") 
    print("___2. Buscar Docente________") 
    print("___3. Eliminar Docente______") 
    op=int(input())
    return op
#Submenu estudiantes
def menu_estudiantes() :
    print(".................................") 
    print("___MENU ESTUDIANTES____________") 
    print("___1. Crear Estudiante_________") 
    print("___2. Buscar Estudiante________") 
    print("___3. Eliminar Estudiante______") 
    op=int(input())
    return op
#Submenu matriculas
def menu_matriculas() :
    print("................................") 
    print("___MENU MATRICULAS____________") 
    print("___1. Crear Matricula_________") 
    print("___2. Buscar Matricula________") 
    print("___3. Eliminar Matricula______") 
    op=int(input())
    return op
#Submenu reportes
def menu_reportes() :
    print("....................................................") 
    print("___MENU REPORTES__________________________________") 
    print("___1. Listado de matriculados por materia_________") 
    print("___2. Buscar matriculados por curso_______________")  
    print("___3. Buscar listado de profesores________________") 
    print("___4. Buscar listado de estudiantes________________") 
    op=int(input())
    return op

#Funcion para crear estudiantes en diccionario y guardarlo como json
def crearEstudiante(seq) :
    estudiante={}
    codigo_estudiante = seq
    nombres=input("Ingrese los nombres:").upper()
    apellidos=input("Ingrese los apellidos:").upper()
    telefono=input("Ingrese el telefono:").upper()
    direccion=input("Ingrese la direccion:").upper()    
    estudiante['codigo_estudiante']=codigo_estudiante
    estudiante['nombre']=nombres
    estudiante['apellido']=apellidos
    estudiante['telefono']=telefono
    estudiante['direccion']=direccion    
    global datos_estudiantes
    datos_estudiantes['Estudiantes'].append(estudiante)
    guardar_json('GuardaEstudiante')
    

#Funcion para crear Docentes en diccionario y guardarlo como json
def crearDocente(seq) :
    docente={}
    codigo_docente = seq
    nombres=input("Ingrese los nombres:").upper()
    apellidos=input("Ingrese los apellidos:").upper()
    telefono=input("Ingrese el telefono:").upper()
    direccion=input("Ingrese la direccion:").upper()
    titulo=input("Ingrese el titulo profesional:").upper()
    nivel=input("Ingrese el nivel de estudios:").upper()    
    docente['codigo_docente']=codigo_docente
    docente['nombre']=nombres
    docente['apellido']=apellidos
    docente['telefono']=telefono
    docente['direccion']=direccion
    docente['titulo']=titulo
    docente['nivel']=nivel    
    global datos_docentes
    datos_docentes['Docentes'].append(docente)
    guardar_json('GuardaDocente')
    

#Funcion para crear Docentes en diccionario y guardarlo como json
def crearMatricula(seq) :
    Matricula={}
    id = seq
    idCurso=input("Ingrese ID del curso:")
    idEstudinate=input("Ingrese el codigo del estudiante:")
    idDocente=input("Ingrese el codigo del docente:")
    Matricula['id']=id
    Matricula['idCurso']=idCurso
    Matricula['idEstudinate']=idEstudinate
    Matricula['idDocente']=idDocente    
    global datos_matricula
    datos_matricula['Matriculas'].append(Matricula)
    guardar_json('GuardaMatricula')
    
#Crea y guarda los archivos json
def guardar_json(t) :
    if t == 'GuardaEstudiante':
        with open('estudiantes.json','w') as f:
            json.dump(datos_estudiantes,f)
    elif t == 'GuardaDocente':
        with open('docentes.json','w') as f:
            json.dump(datos_docentes,f)
    elif t == 'GuardaMatricula':
        with open('matriculas.json','w') as f:
            json.dump(datos_matricula,f)
    
#Carga los archivos json si no los encuentra saca error
def loadData_json(t) :
    
    if t == 'CargaEstudiante':    
        try:
            with open('estudiantes.json','r') as f:
                global datos_estudiantes
                datos_estudiantes=json.load(f)
                lista = []

                for i in range(len(datos_estudiantes['Estudiantes'])) :                    
                    if datos_estudiantes['Estudiantes'][i] :                                                                    
                        lista.append(datos_estudiantes['Estudiantes'][i]['codigo_estudiante'])                                                                            
                        maxi = int(max(lista))                                
                        seq = maxi+1
            return(str(seq))
        except IOError:
            print(" ")
            seq = '1001' 
            return seq

    elif t == 'CargaDocente':           
        try:
            with open('docentes.json','r') as f:
                global datos_docentes
                datos_docentes=json.load(f)
                lista = []
              
                for i in range(len(datos_docentes['Docentes'])) :
                    if datos_docentes['Docentes'][i] :                                                                    
                        lista.append(datos_docentes['Docentes'][i]['codigo_docente'])                                                                            
                        maxi = int(max(lista))                                
                        seq = maxi+1
            return(str(seq))
        except IOError:
            print(" ")
            seq = '1001'
            return seq

    elif t == 'CargaMatricula':    
        try:
            with open('matriculas.json','r') as f:
                global datos_matricula
                datos_matricula=json.load(f)
                lista = []

                for i in range(len(datos_matricula['Matriculas'])) :
                    
                    if datos_matricula['Matriculas'][i] :                                                                    
                        lista.append(datos_matricula['Matriculas'][i]['id'])                                                                            
                        maxi = int(max(lista))                                
                        seq = maxi+1
            return(str(seq))
        except IOError:
            print(" ")
            seq = '1001'
            return seq

    elif t == 'CargaCursos':
        try:
            with open('cursos.json','r') as f:
                global datos_cursos
                datos_cursos=json.load(f)                                                                                                                              
        except IOError:
            print(" ")
    
#parametros(cadena a buscar,diccionario a buscar,columna a buscar)
def buscar(nombre,dicc, columna):     
    lista =[]
    
    if  dicc == 'datos_docentes':           
        if datos_docentes['Docentes']:
            for i in range(len(datos_docentes['Docentes'])) :  
                if   datos_docentes['Docentes'][i][columna]  :                                                                                              
                    nom= datos_docentes['Docentes'][i][columna]
                    busca = nom.find(nombre)
                    if busca != -1:
                        lista.append(i)
        return lista
    if  dicc == 'datos_estudiantes':    
        if datos_estudiantes['Estudiantes']:
            for i in range(len(datos_estudiantes['Estudiantes'])) :  
                if datos_estudiantes['Estudiantes'][i][columna]:              
                    nom= datos_estudiantes['Estudiantes'][i][columna]
                    busca = nom.find(nombre)
                    if busca != -1:
                        lista.append(i)
        return lista
    elif dicc == 'datos_matricula':   
        if datos_matricula['Matriculas']:
            for i in range(len(datos_matricula['Matriculas'])) :                                                                                          
                #if datos_matricula['Matriculas'][i][columna]:
                nom= datos_matricula['Matriculas'][i][columna]
                busca = nom.find(nombre)
                if busca != -1:
                    lista.append(i)
            return lista            
    elif dicc == 'datos_cursos':   
        if datos_cursos['Cursos']:
            for i in range(len(datos_cursos['Cursos'])) :                                                                                          
                #if datos_matricula['Matriculas'][i][columna]:
                nom= datos_cursos['Cursos'][i][columna]
                busca = nom.find(nombre)
                if busca != -1:
                    lista.append(i)
            return lista

#Reportes
def mostrarReporte(t) :
    loadData_json('CargaMatricula')                     
    loadData_json('CargaCursos')
    loadData_json('CargaDocente')
    loadData_json('CargaEstudiante')

    if t == 'reporte1':
      
        print("")
        print("------------------------------------------------------------------------------------------------")
        if datos_matricula['Matriculas']:
            
            print('|','MATRICULA' ,'|','\t     ESTUDIANTE \t','|','\t     DOCENTE\t','        |','\tCURSO\t','      |' )
            print("------------------------------------------------------------------------------------------------")
            for i in range(len(datos_matricula['Matriculas'])) :                                    
                    estudiante = datos_matricula['Matriculas'][i]['idEstudinate']
                    docente = datos_matricula['Matriculas'][i]['idDocente']
                    curso = datos_matricula['Matriculas'][i]['idCurso']
                    res_est = buscar( estudiante,'datos_estudiantes','codigo_estudiante')                    
                    res_doc = buscar( docente,'datos_docentes','codigo_docente')                    
                    res_cur = buscar( curso,'datos_cursos','Id_curso')                    
                    #print('estu',res_est)
                    #print('doce',res_doc)
                    #print('cur',res_cur)
                    print('|' ,datos_matricula['Matriculas'][i]['id'],'     |','\t',datos_estudiantes['Estudiantes'][res_est[0]]['nombre'],' ',datos_estudiantes['Estudiantes'][res_est[0]]['apellido'],'\t','|','\t',datos_docentes['Docentes'][res_doc[0]]['nombre'],' ',datos_docentes['Docentes'][res_doc[0]]['apellido'],'  \t |','  ',datos_cursos['Cursos'][res_cur[0]]['nombreCurso'],'      |')
                    print("------------------------------------------------------------------------------------------------")
            print("")
    elif t == 'reporte2':
        
        print("")
        
        for i in range(len(datos_cursos['Cursos'])) :            
                print("------------------------------------------")
                print('|','\t CURSO: \t' , datos_cursos['Cursos'][i]['nombreCurso'],'\t','|')
                print("------------------------------------------")
                curso= datos_cursos['Cursos'][i]['Id_curso']                
                res_cur = buscar(curso,'datos_matricula','idCurso')     
                #print(res_cur)             
                print('|','CODIGO ','|','NOMBRE ESTUDIANTE','|','CELULAR','|')
                print("------------------------------------------")
                for i in range (len(res_cur)):
                    est=buscar(datos_matricula['Matriculas'][i]['idEstudinate'],'datos_estudiantes','codigo_estudiante')                        
                    if est:
                        #print('|','CODIGO ','|','NOMBRE ESTUDIANTE','|','CELULAR','|')
                        for i in range (len(est)):
                            j= est[i] 
                            print('|',datos_estudiantes['Estudiantes'][j]['codigo_estudiante'], '   |', datos_estudiantes['Estudiantes'][j]['nombre'], ' ',datos_estudiantes['Estudiantes'][j]['apellido'],'  |',datos_estudiantes['Estudiantes'][j]['telefono'],'   |')                        
                print("------------------------------------------\n")
    elif t =='reporte3':
        if datos_docentes['Docentes']:
            print("---------------------------------------------------------------------------")
            print('|','CODIGO ','|','NOMBRE ','|','APELLIDO ','|','CELULAR','|','DIRECCION ','|','TITULO ','|','NIVEL ','|')
            print("---------------------------------------------------------------")
            for i in range (len(datos_docentes['Docentes'])):
                print('|',datos_docentes['Docentes'][i]['codigo_docente'],'   |',datos_docentes['Docentes'][i]['nombre'],'   |',datos_docentes['Docentes'][i]['apellido'],'    |',datos_docentes['Docentes'][i]['telefono'],'   |',datos_docentes['Docentes'][i]['direccion'],'    |',datos_docentes['Docentes'][i]['titulo'],'  |',datos_docentes['Docentes'][i]['nivel'],'    |' )
            print("---------------------------------------------------------------\n")
    elif t =='reporte4':
        if datos_estudiantes['Estudiantes']:
            print("---------------------------------------------------------------------------")
            print('|','CODIGO ','|','NOMBRE ','|','APELLIDO ','|','CELULAR','|','DIRECCION ','|')
            print("---------------------------------------------------------------")
            for i in range (len(datos_estudiantes['Estudiantes'])):
                print('|',datos_estudiantes['Estudiantes'][i]['codigo_estudiante'],'   |',datos_estudiantes['Estudiantes'][i]['nombre'],'   |',datos_estudiantes['Estudiantes'][i]['apellido'],'    |',datos_estudiantes['Estudiantes'][i]['telefono'],'   |',datos_estudiantes['Estudiantes'][i]['direccion'],'    |')
            print("---------------------------------------------------------------\n")
#/////////////////////////////////////////////////////////////////////////////////////
                                #Inicio programa
#/////////////////////////////////////////////////////////////////////////////////////
#Genera json de los cursos predefinidos
with open('cursos.json','w') as f:
    json.dump(datos_cursos,f)

op=menu_principal()

while op>=1 and op<5 :
    
#**************************************************************************************************  
                                        #MENU DOCENTES
#**************************************************************************************************  
    if op==1:        
        print("")        
        sm=menu_docentes()               
        if sm == 1:
            print(".....Crear Docente.....")
            seq = loadData_json('CargaDocente')            
            crearDocente(seq)
            print("........................ \n")
        elif sm == 2:            
            print(".....Buscar Docente.....")
            loadData_json('CargaDocente') 
            nombre=input("ingrese nombre a buscar:").upper()
            resultado= buscar(nombre,'datos_docentes','nombre')                      
            #imprime los datos encontrados
            print("")
            print("------------------------------------------")
            for i in range(len(resultado)) :  
                j=resultado[i]              
                print("Codigo_docente: ",datos_docentes['Docentes'][j]['codigo_docente'])
                print("Nombre: ",datos_docentes['Docentes'][j]['nombre'])
                print("Apellidos: ",datos_docentes['Docentes'][j]['apellido'])
                print("Telefono: ",datos_docentes['Docentes'][j]['telefono'])
                print("Direccion: ",datos_docentes['Docentes'][j]['direccion'])
                print("Titulo: ",datos_docentes['Docentes'][j]['titulo'])
                print("Nivel: ",datos_docentes['Docentes'][j]['nivel'])              
                    
                print("------------------------------------------")
            print("")
                                
        elif sm == 3:
            print(".....Eliminar Docente.....")
            loadData_json('CargaMatricula') 
            nombre=input("ingrese id del docente que desea eliminar:")
            resultado= buscar(nombre,'datos_matricula','idDocente')                                  
            print("")
            print("------------------------------------------")
            loadData_json('CargaDocente')             
            ##print("Codigo_docente: ",datos_matricula['Matriculas'])
            if resultado: 
                for i in range(len(resultado)) :  
                    j=resultado[i]              
                    print('El docente ',datos_docentes['Docentes'][j]['nombre'], ' no se puede eliminar ya tiene matricula')                            
            else:                           
                resultado= buscar(nombre,'datos_docentes','codigo_docente')  
                if resultado:
                    for i in range(len(resultado)) :  
                        j=resultado[i]
                        del(datos_docentes['Docentes'][j])
                        print('docente eliminado')
                        guardar_json('GuardaDocente')
            print("------------------------------------------")
        
#**************************************************************************************************
                                    #MENU ESTUDIANTES
#**************************************************************************************************  
    elif op==2:
        print("")
        sm=menu_estudiantes()
        if sm == 1:
            print(".....Crear Estudiante.....")
            seq = loadData_json('CargaEstudiante')
            crearEstudiante(seq)
            print("........................ \n")
        elif sm == 2:
            print(".....Buscar Estudiante.....")
            loadData_json('CargaEstudiante') 
            nombre=input("ingrese nombre a buscar:").upper()
            resultado= buscar(nombre,'datos_estudiantes','nombre') 
            print(resultado)                     
            #imprime los datos encontrados
            print("")
            print("------------------------------------------")
            for i in range(len(resultado)) :  
                j=resultado[i]              
                print("Codigo_estudiante: ",datos_estudiantes['Estudiantes'][j]['codigo_estudiante'])
                print("Nombre: ",datos_estudiantes['Estudiantes'][j]['nombre'])
                print("Apellidos: ",datos_estudiantes['Estudiantes'][j]['apellido'])
                print("Telefono: ",datos_estudiantes['Estudiantes'][j]['telefono'])
                print("Direccion: ",datos_estudiantes['Estudiantes'][j]['direccion'])                        
                        
                print("------------------------------------------")
            print("")        
        elif sm == 3:
            print(".....Eliminar Estudiante.....")
            loadData_json('CargaMatricula') 
            nombre=input("ingrese id del estudiante que desea eliminar:")
            resultado= buscar(nombre,'datos_matricula','idEstudinate')                                  
            print("")
            print("------------------------------------------")
            loadData_json('CargaEstudiante')             
            ##print("Codigo_docente: ",datos_matricula['Matriculas'])
            if resultado: 
                for i in range(len(resultado)) :  
                    j=resultado[i]                                 
                    print('El Estudiante ',  datos_estudiantes['Estudiantes'][j]['nombre'] ,' no se puede eliminar ya tiene matricula')                            
            else:                           
                resultado= buscar(nombre,'datos_estudiantes','codigo_estudiante')  
                if resultado:
                    for i in range(len(resultado)) :  
                        j=resultado[i]
                        del(datos_estudiantes['Estudiantes'][j])
                        print('Estudiante eliminado')
                        guardar_json('GuardaEstudiante')
            print("------------------------------------------")

#**************************************************************************************************   
                                        #MENU MATRICULAS
#**************************************************************************************************  
    elif op==3:
        print("")        
        sm = menu_matriculas()
        if sm == 1:
            print(".....Crear Matricula.....")
            seq = loadData_json('CargaMatricula') 
            crearMatricula(seq)
            print("........................ \n")
        elif sm == 2:
            print(".....Buscar Matricula.....")
            loadData_json('CargaMatricula')      
            nombre=input("ingrese id de la matricula:")
            resultado= buscar(nombre,'datos_matricula','id')                      
            #imprime los datos encontrados
            print("")
            print("------------------------------------------")
            for i in range(len(resultado)) :  
                j=resultado[i]              
                print("Id_matricula: ",datos_matricula['Matriculas'][j]['id'])
                print("Id_curso: ",datos_matricula['Matriculas'][j]['idCurso'])
                print("id_estudiante: ",datos_matricula['Matriculas'][j]['idEstudinate'])
                print("id_docente: ",datos_matricula['Matriculas'][j]['idDocente'])
                                    
                print("------------------------------------------")
            print("")
        elif sm == 3:
            print(".....Eliminar Matricula.....")             
            loadData_json('CargaMatricula') 
            nombre=input("ingrese id de la matricula que desea eliminar:")
            resultado= buscar(nombre,'datos_matricula','id')                                  
            print("")
            print("------------------------------------------")
            loadData_json('CargaEstudiante')             
            if resultado:
                for i in range(len(resultado)) :  
                    j=resultado[i]
                    del(datos_matricula['Matriculas'][j])
                    print('Matricula eliminada')
                    guardar_json('GuardaMatricula')        
            print("------------------------------------------")  

#**************************************************************************************************  
                                        #MENU REPORTES
#**************************************************************************************************      
    elif op==4:
        print("")        
        sm = menu_reportes()
        if sm == 1:
            print(".....LISTADO POR MATRICULAS .....")
            mostrarReporte('reporte1')
            print("||||||||||||||||||||||||| \n")
        elif sm == 2:
            print(".....LISTADO MATRICULADOS POR CURSO.....")
            mostrarReporte('reporte2')                 
            print("||||||||||||||||||||||||| \n") 
        elif sm == 3:
            print(".....LISTADO DE PROFESORES.....")
            mostrarReporte('reporte3')                 
            print("||||||||||||||||||||||||| \n") 
        elif sm == 4:
            print(".....LISTADO DE ESTUDIANTES.....")
            mostrarReporte('reporte4')                 
            print("||||||||||||||||||||||||| \n") 
    
    op=menu_principal() 
 