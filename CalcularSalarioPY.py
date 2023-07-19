


# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 00:07:01 2022

@author: Estefanyt
Programa que permite calcular el salario mensual y el sueldo neto ,segun los impuestos del ISS,AFP,SAR,RENTA, teniendo en cuenta
que el sueldo ingresado
"""
planilla={
    "codigos":[],
    "nombres":[],
    "apellidos":[],
    "Puesto":[],
    "ISSS_E":[],#ISS
    "AFP_E":[],#AFP
    "SAR_E":[],#SAR
    "RENTA":[],#RENTA
    "Sueldo_Mensual":[],
    "Sueldo_Neto":[]
    }
ejecutar = True

while ejecutar:
    print("-"*62)
    print("-"*15,"OPCIONES DEL PROGRAMA PLANILLA","-"*15)
    print("\n")
    
    #Aqui comienza menu de opciones
    
    print("1)=> Agregar Nuevo Empleado: ")
    print("2)=> Modificar los Datos de los Empleado: ")
    print("3)=> Mostrar Planilla de Empleados: ")
    print("4)=> Buscar Empleado: ")
    print("5)=> Salir del Programa")
    print("\n")
    op= int(input("Acción a realizar: "))

#Inicio de campo registro---------------------------------------------------------
    if op==1:
        print("INGRESO DE DATOS DE EMPLEADO-------------------------=>")
        print("\n")
        codigoE=input("Asigne un Codigo al Empleado: ").title()
        found=False
        for i in range(len(planilla["codigos"])):
            if planilla["codigos"][i]==codigoE:
                found=True
                print("Codigo de Empleado ya Exite")
                print("Pruebe con uno nuevo o busque empleado asociado al codigo: ")
        if not found:
            nombreE=input("Ingrese Nombre del Empleado: ").title()
            apellidoE=input("Ingrese Apellido del Empleado: ").title()
            puestoE=input("Ingrese Puesto del Empleado: ").title()
            sueldoE=float(input("Ingrese Sueldo del Empleado: $"))
            planilla["codigos"].append(codigoE)
            planilla["nombres"].append(nombreE)
            planilla["apellidos"].append(apellidoE)
            planilla["Puesto"].append(puestoE)
            planilla["Sueldo_Mensual"].append(sueldoE)
            
            #----- INICIO SCalculos de decuentos en registro ---------
            
            ISSS=sueldoE*0.03 
            AFP=sueldoE*0.0725 
            planilla["ISSS_E"].append(ISSS)
            planilla["AFP_E"].append(AFP)
            
            SAR=sueldoE-(ISSS+AFP)
            planilla["SAR_E"].append(SAR)
            
            if SAR >= 1 and SAR < 500:
                RENTA=0
                Sueldo_Neto=SAR
                
                planilla["RENTA"].append(RENTA)
                planilla["Sueldo_Neto"].append(Sueldo_Neto)
                
            elif SAR >= 500 and SAR <1000:
                RENTA=SAR*0.10
                Sueldo_Neto=SAR-RENTA
                
                planilla["RENTA"].append(RENTA)
                planilla["Sueldo_Neto"].append(Sueldo_Neto)
                
            elif SAR>1000:
                RENTA=SAR*0.20
                Sueldo_Neto=SAR-RENTA
                planilla["RENTA"].append(RENTA)
                planilla["Sueldo_Neto"].append(Sueldo_Neto)
                
            else:
                
                print("Sueldo no deben ser menos de $ 1")
                
            #----- FIN Calculos de decuentos registro ---------
        input()
#Fin de campo registro--------------------------------------------------------------
#
#Inicio de campo Modificar----------------------------------------------------------
    elif op==2:
        print("MODIFICACION DE DATOS DE EMPLEADO-------------------------=>")
        modificarE=input("Ingrese el Codigo del Emplado para Modificar los datos: ").title()
        found=False
        for i in range(len(planilla["codigos"])):
            found=True
            if planilla["codigos"][i]==modificarE:
                print("Que datos desea M0dificar")
                print("1)=> Nombre del Empleado: ")
                print("2)=> Apellido del Empleado: ")
                print("3)=> Ingrese Puesto del Empleado: ")
                print("4)=> Sueldo del Empleado: ")
                opcMo = int(input("Opcion: "))
                if opcMo==1:
                    nombreE=input("Ingrese Nombre del Empleado: ").title()
                    planilla["nombres"][i]=nombreE
                    input()
                elif opcMo==2:
                    apellidoE=input("Ingrese Apellido del Empleado: ").title()
                    planilla["apellidos"][i]=apellidoE
                elif opcMo==3:
                    puestoE=input("Ingrese Puesto del Empleado: ").title()
                    planilla["Puesto"][i]=puestoE
                    input()
                elif opcMo==4:
                    print("Tenga en Cuenta que al Modificar el Sueldo se modificara el Sueldo Neto")
                    sueldoE=float(input("Ingrese Sueldo del Empleado: $"))
                    planilla["Sueldo_Mensual"][i]=sueldoE
                    
                    ISSS=sueldoE*0.03
                    AFP=sueldoE*0.0725
                    planilla["ISSS_E"][i]=ISSS
                    planilla["AFP_E"][i]=AFP
                    
                    SAR=sueldoE-(ISSS+AFP)
                    planilla["SAR_E"][i]=SAR
                    
                    if SAR >= 1 and SAR < 500:
                        RENTA=0
                        Sueldo_Neto=SAR
                        planilla["Sueldo_Neto"][i]=Sueldo_Neto
                        planilla["RENTA"][i]=RENTA
                        
                    elif SAR >= 500 and SAR <1000:
                        RENTA=SAR*0.10
                        Sueldo_Neto=SAR-RENTA
                        planilla["Sueldo_Neto"][i]=Sueldo_Neto
                        planilla["RENTA"][i]=RENTA
                        
                    elif SAR>1000:
                        RENTA=SAR*0.20
                        Sueldo_Neto=SAR-RENTA
                        planilla["Sueldo_Neto"][i]=Sueldo_Neto
                        planilla["RENTA"][i]=RENTA
                        
                    else:
                        print("Sueldo no deben ser menos de $ 1")
                    print("Modificaion con exito...")
        if not found:
            print("El Codigo No esta Registrado")
        input()
#Fin de campo Modificar-----------------------------------------------------------
#---------------------------------------------------------------------------------
#ORDENA PLANTILLA-----------------------------------------------------------------
    elif op==3:
        print("Planilla de Empleados-------------------------=>")
        listaOrdenada=sorted(planilla["apellidos"])
        for i in listaOrdenada:
            print("----------------------------------------------------------")  
            for j in range(len(planilla["apellidos"])):
                if planilla["apellidos"][j]==i:
                    print("| APELLIDO: ", planilla["apellidos"][j], end=" ")
                    print("| NOMBRE: ", planilla["nombres"][j])
                    print("| SUELDO: ", planilla["Sueldo_Mensual"][j],end=" ")
                    print("| ISS: ", planilla["ISSS_E"][j], end=" ")
                    print("| AFP: ", planilla["AFP_E"][j], end=" ")
                    print("| SAR: ", planilla["SAR_E"][j], end=" ")
                    print("| RENTA: ", planilla["RENTA"][j])
                    print("| SUELDO NETO: ", planilla["Sueldo_Neto"][j], end=" ")
                    print("| PUESTO: ", planilla["Puesto"][j], end=" ")
                    print("| CODIGO: ", planilla["codigos"][j],)
        input()
#Fin-------------------------------------------------------------------------------
#Inicio empleado--------------------------------------------------------------------
    elif op==4:
        consultaE=input("Ingres el Codigo del empleado: ").title()
        print("DATOS DEL EMPLEADO-------------------------=>")
        print()
        found=False
        for i in range(len(planilla["codigos"])):
            found=True
            if planilla["codigos"][i]==consultaE:
                print("| APELLIDO: ", planilla["apellidos"][i])
                print("| NOMBRE: ", planilla["nombres"][i])
                print("| SUELDO: ", planilla["Sueldo_Mensual"][i])
                print("| ISS: ", planilla["ISSS_E"][i])
                print("| AFP: ", planilla["AFP_E"][i])
                print("| SAR: ", planilla["SAR_E"][i])
                print("| RENTA: ", planilla["RENTA"][i])
                print("| SUELDO NETO: ", planilla["Sueldo_Neto"][i])
                print("| PUESTO: ", planilla["Puesto"][i])
                print("| CODIGO: ", planilla["codigos"][i])
                print()
        if not found:
            print("El Codigo No esta Registrado")
        input()
#Fin----------------------------------------------------------------------------------     
    elif op==5:
        ejecutar = False
        print("\n")
        print("Programa Terminado...")
        print("-"*62)
        print("\n")
    else:
        print("-"*62)
        print("Opcion no valida...")
        print("Ejecute una opcion valida...")
        print("\n")
        input()
