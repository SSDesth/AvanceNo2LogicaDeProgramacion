#Integrantes del Proyecto
#Carlos Andres Montero Moreno
#Keila Nicole Silva Montes
#Mery Hellen Cordero Carpio

#Declaracion de varibales

ejecucionPrograma = True
reportes = []

while(ejecucionPrograma):

    reporte = { "reporteCreado": "",
        "descripcion" : "",
        "llamadoAmbulancia" : "",
        "llamadoFuerzaPublica" : "",
        "sitacionPeligrosa" : "",
        "alejarseDelLugar": ""     
        }
    
    print("---------- Menu ----------")
    print("1. Reportar una actividad sospechosa.")
    print("2. No reportar una actividad sospechosa.")
    print("3. Salir.")
    valorUsuario = input("Ingrese una opción: ")

    if (valorUsuario == "1"):
        print("---------- Opción 1 ----------")
        print("Se va a generar un reporte de seguridad")

        reporte["reporteCreado"] = "Reporte Creado"
        reporte["descripcion"] = "Actividad sospechosa"
        
        opcionesCorrecta = False

        while(opcionesCorrecta== False):
            print("---------- Menu opción 1.1 ----------")
            print("1. Reportar un herido")
            print("2. No hay heridos")
            valorUsuarioOpcion1 = input("Ingrese una opción: ")

            if(valorUsuarioOpcion1 == "1"):
                print("Se hace un llamado por una ambulancia")
                reporte["llamadoAmbulancia"] = "Se hace un llamado a la ambulancia"
                opcionesCorrecta = True
            elif(valorUsuarioOpcion1 == "2"):
                reporte["llamadoAmbulancia"] = "No se hace un llamado a la ambulancia"
                opcionesCorrecta = True
                
            else:
                print("---------- Error ----------")
                print("La opción ingresada '" + valorUsuarioOpcion1 + "' no es valida")
                
        print("Se va a llamar a la fuerza pública")
        reporte["llamadoFuerzaPublica"] = "Se hace un llamado a la fuerza pública"
        
        opcionesCorrecta = False

        while(opcionesCorrecta== False):
            print("---------- Menu opción 1.2 ----------")
            print("1. La situación es peligrosa")
            print("2. La situación no es peligrosa")
            valorUsuarioOpcion1 = input("Ingrese una opción: ")

            if(valorUsuarioOpcion1 == "1"):
                print("Favor buscar refugio hasta que la situación no sea peligrosa")
                reporte["sitacionPeligrosa"] = "Se busco un refujio por situación peligrosa"
                opcionesCorrecta = True
            elif(valorUsuarioOpcion1 == "2"):
                reporte["sitacionPeligrosa"] = "No se busco un refujio por situación peligrosa"
                opcionesCorrecta = True
            else:
                print("---------- Error ----------")
                print("La opción ingresada '" + valorUsuarioOpcion1 + "' no es valida")

        print("Favor Alejarse del lugar")
        reporte["alejarseDelLugar"] = "La persona que reporto se alejó del lugar"

        print("--------- Resumen del reporte ---------")
        print("")
        
        for  elemento in reporte.values():
            print(elemento)

        print("")
              
    elif(valorUsuario == "2" ):
        print("---------- Opción 2 ----------")
        print("No se genera ningún reporte")

    elif(valorUsuario == "3" ):
        ejecucionPrograma = False

    else:
        print("---------- Error ----------")
        print("La opción ingresada '" + valorUsuario + "' no es valida")


print("-------- Final Programa --------")

