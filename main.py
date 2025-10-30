#Cogigo main

from _pycache_.Funciones import *

'''
Inicializamos las listas que nos da el ejercicio
'''

lista_centro_logistico = ["Buenos Aires","San Juan","Jujuy","Neuquén"]
lista_insumos_basicos = ["Guantes descartables","Mascarillas quirúrgicas", "Jeringas","Alcohol en gel",
                         "Test rápidos"]

ejecutador = True

'''
Creamos un bucle para que el usuario pueda
cargar datos hasta que determine que quiere salir
'''

while ejecutador == True:
    print("Iniciando")
    print("------------------------------------------------")
    print("Bienvenido, por favor, eliga una de las siguientes opciones: ")
    print("1. Cargar stocks de insumos")
    print("2. Ver los centros con mas de 10000 unidades de stock totales")
    print("3. Ver insumos con mas de 7000 unidades de stock")
    print("4. Ver el centro con mayor cantidad de cada insumo")
    print("5. Registrar las ventas de insumos")
    print("6. Informe de ventas por centro")
    print("7. Informe de ventas por insumo de cada centro")
    print("8. Informe de reposicion de stock")
    print("9. Porcentaje de stock de cada insumo respecto al total")
    print("10. Terminar de consultar.")
    selector_opciones = int(input("Ingrese una de las previas opciones: "))

    '''
    Dentro del bucle, le damos las opciones para que decida que hacer con el programa.
    Si pone algo que no es correcto, marca error y te devuelve al selector de opciones.
    '''

    match selector_opciones:
        case 1:
            '''
            Creamos y cargamos una matriz con los datos.
            '''
            matriz_insumos = crear_matriz(lista_centro_logistico,lista_insumos_basicos)
            insumos_cargados = cargar_insumos(matriz_insumos,lista_insumos_basicos,lista_centro_logistico,
                                              "Cargar insumos de ")
            '''
            Bucle para que nos salga en pantalla, los datos ingresados
            '''
            for i in range(len(insumos_cargados)):
                print(f"En la cede de {lista_centro_logistico[i]} hay: ")
                for j in range(len(insumos_cargados[i])):
                    print(f"{insumos_cargados[i][j]} unidades de: {lista_insumos_basicos[j]}" "\n")
        case 2:
            if insumos_cargados != [None]:
                lista_unidades_mayores_10000 = [] * len(lista_centro_logistico)
                print(f"Los centros con mas de 10000 unidades son/es: ")
                for i in range(len(insumos_cargados)):
                    valor = sumar_listas(insumos_cargados[i])
                    lista_unidades_mayores_10000 += [valor]
                    if lista_unidades_mayores_10000[i] > 10000:
                        print(f"{lista_centro_logistico[i]}")  
            else:
                print("No a cargado ningun dato, por favor, vuelva al punto 1.")
        case 3:
            matriz_insumos_orden_contrario = crear_matriz(lista_insumos_basicos,lista_centro_logistico)
            insumos_cargados_contrario = cargar_insumos(matriz_insumos_orden_contrario,lista_centro_logistico,
                                                        lista_insumos_basicos,
                                                        "Cargar insumos de")
            '''
            Creo una nueva matriz con orden alrevez. Filas por insumos, columnas por centros.
            Luego, repito el modus operandi del segundo caso.
            '''
            if insumos_cargados_contrario != [None]:
                lista_unidades_mayores_7000 = [] * len(lista_insumos_basicos)
                print(f"Los insumos basicos con mas de 7000 unidades son/es: ")
                for i in range(len(insumos_cargados_contrario)):
                    valor = sumar_listas(insumos_cargados_contrario[i])
                    lista_unidades_mayores_7000 += [valor]
                    if lista_unidades_mayores_7000[i] > 7000:
                        print(f"{lista_insumos_basicos[i]}")  
        case 4:
            if insumos_cargados != [None]:
                for i in range(len(insumos_cargados_contrario)):
                   print(f"En el insumo: {lista_insumos_basicos[i]} el centro que tiene mas unidades es: ")
                   indice = 0
                   cantidad_centro = 0
                   for j in range(len(insumos_cargados_contrario[i])):
                        if cantidad_centro > insumos_cargados_contrario[i][j]:
                            cantidad_centro = insumos_cargados_contrario[i][j]
                            indice = j
                        print(f"{lista_centro_logistico[indice]}")
            else:
                print("Los insumos no se han cargado.")
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            matriz_diferencial_vacia = crear_matriz(lista_centro_logistico,lista_insumos_basicos)
            matriz_diferencial_cargada = cargar_insumos_diferenciales(matriz_diferencial_vacia,
                                                                      insumos_cargados,"")
            '''
            Creamos una matriz que contenga el resultado de la diferencia
            entre el numero deseado, y la matriz de carga.
            '''
            if insumos_cargados != [None]:
                for i in range(len(insumos_cargados)):
                    print(f"El diferencial en el centro {lista_centro_logistico[i]} por insumo es de: ")
                    for j in range(len(insumos_cargados[i])):
                        print(f"{matriz_diferencial_cargada[i][j]} unidades, para el insumo: {lista_insumos_basicos[j]}")
            else:
                print("Los insumos no se han cargado.")

        case 9:
            matriz_insumos = crear_matriz(lista_centro_logistico,lista_insumos_basicos)
            insumos_cargados = cargar_insumos(matriz_insumos,lista_insumos_basicos,lista_centro_logistico,
                                              "Cargar insumos de ")
            
            lista_stock_fila = [] * len(lista_centro_logistico)
            for i in range(len(insumos_cargados)):
                primer_valor = sumar_listas(insumos_cargados[i])
                lista_stock_fila += [primer_valor]
            for i in range(len(lista_stock_fila)):
                valor_total_stock = sumar_listas(lista_stock_fila[i])
            for i in range(len(lista_stock_fila)):
                porcentaje = lista_stock_fila[i]*100/valor_total_stock[0]
                print(f"El porcentaje del insumo {lista_insumos_basicos[i]} es igual a: {porcentaje}")
        case 10:
            ejecutador = False
        case _:
            print("La opcion elegida no es existente. Por favor, ingrese una opcion correcta.")