fecha = input("INGRESE LA FECHA ACTUAL EN FORMATO (dia, DD/MM): ").lower()

dia_semana = fecha[0:fecha.find (',')]

dia = int (fecha[fecha.find (' ') +1 : fecha.find("/")  ])

mes = int (fecha [fecha.find('/')+1:])

if (dia < 1 or dia > 31 or mes < 1 or mes > 12):
    print("ERROR: VALORES INVALIDOS!")
elif (dia_semana == "lunes"):
    print ("El dia de la semana es",dia_semana,dia,"/",mes)
    print("DIA DE EXAMEN NIVEL INICIAL")
    alumnos_aprobado = int (input ("INGRESE LA CANTIDAD DE ALUMNOS APROBADOS: "))
    alumnos_desaprobado = int (input ("INGRESE LA CANTIDAD DE ALUMNOS DESAPROBADOS: "))
    
    porcentaje_aprobados = (alumnos_aprobado*100)//(alumnos_aprobado + alumnos_desaprobado)
    
    print("EL PORCENTAJE DE ALUMNOS APROBADOS ES: ",porcentaje_aprobados,"%")
elif (dia_semana == "martes"):
    print ("El dia de la semana es",dia_semana,dia,"/",mes)
    print("DIA DE EXAMEN NIVEL INTERMEDIO")
    alumnos_aprobado = int (input ("INGRESE LA CANTIDAD DE ALUMNOS APROBADOS: "))
    alumnos_desaprobado = int (input ("INGRESE LA CANTIDAD DE ALUMNOS DESAPROBADOS: "))
    
    porcentaje_aprobados = (alumnos_aprobado*100)//(alumnos_aprobado + alumnos_desaprobado)
    
    print("EL PORCENTAJE DE ALUMNOS APROBADOS ES: ",porcentaje_aprobados,"%")
elif (dia_semana == "miercoles"):
    print ("El dia de la semana es",dia_semana,dia,"/",mes)
    print("DIA DE EXAMEN NIVEL AVANZADO")
    alumnos_aprobado = int (input ("INGRESE LA CANTIDAD DE ALUMNOS APROBADOS: "))
    alumnos_desaprobado = int (input ("INGRESE LA CANTIDAD DE ALUMNOS DESAPROBADOS: "))
    
    porcentaje_aprobados = (alumnos_aprobado*100)//(alumnos_aprobado + alumnos_desaprobado)
    
    print("EL PORCENTAJE DE ALUMNOS APROBADOS ES: ",porcentaje_aprobados,"%")
elif (dia_semana == "jueves"):
    print ("El dia de la semana es",dia_semana,dia,"/",mes)
    porcentaje_asistencia = int (input ("INGRESE EL PORCENTAJE DE ASISTENCIA: "))
    if (porcentaje_asistencia < 0 or porcentaje_asistencia > 100 ):
        print("ERROR")
    elif(porcentaje_asistencia >= 50):
        print("ASISTIO LA MAYORIA")
    else:
        print("NO ASISTIO LA MAYORIA")
elif (dia_semana == "viernes"):
    print ("El dia de la semana es",dia_semana,dia,"/",mes)
    if (dia == 1 and mes == 1 or mes == 7):
        print("COMIENZO DE NUEVO CICLO")
        
        cantidad_alumnos = int (input ("INGRESE LA CANTIDAD DE ALUMNOS DEL NUEVO CICLO: "))
        arancel = 10000
        total = arancel * cantidad_alumnos
        
        print("EL ARANCEL POR ALUMNO ES DE $",arancel," Y EL TOTAL ES $",total)
    else:
        print("CICLO COMENZADO")
    


