#Pagina de funciones

def crear_matriz(hospitales,insumos):
    '''
    Crea una matriz con cantidad de filas y columnas determinadas previamente.
    '''
    matriz = []
    for i in range(len(hospitales)):
        fila = [0] * len(insumos)
        matriz += [fila]
    return matriz

def cargar_insumos(matriz: list,lista: list,lista2: list, numero = 0)->list:
    '''
    Le asigna valores a la matriz deseada.
    '''
    for i in range(len(matriz)):
        print(f" {lista2[i]}")
        for j in range(len(matriz[i])):
            numero = int(input(f"{lista[j]}: "))
            matriz[i][j] = numero
    return matriz

def cargar_insumos_diferenciales(matriz,matriz2, numero = 500):
    '''
    Funcion en la cual se hace la diferencia entre una matriz y un parametro.
    El resultado es una matriz con la diferencia de los elementos.
    '''
    numero = int(input("Ingrese un numero diferencial: "))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = numero - matriz2[i][j]
    return matriz

def sumar_listas(lista: list):
    '''
    Funcion para sumar los datos dentro de una lista determinada.
    '''
    valor = 0
    contador = 0
    for i in range(len(lista)):
        valor += lista[i]
        if valor >= 10000:
            contador += 1
    return valor