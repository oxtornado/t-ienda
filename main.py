import json

#Funcion encargada de mostrar el menu de la tienda
def menu():

    #Imprimimos el menu
    print('''
==================== Tienda Danielo's ====================
=============Bienvenido, a continuacion puede: ===========
            | 1. Cargar lista
            | 2. Mostrar lista
            | 3. Agregar un producto
            | 4. Eliminar un producto
            | 5. Salir
==========================================================
''')
    
    #Preguntamos que opcion queiere llevar a cabo
    primer_input = int(input('Ingrese el numero de la accion que desa llevar a cabo: '))
    
    #Control de la respuesta con un match porque es una estructura de control 
    # excelente para el control de casos especificos
    match primer_input:
        case 1:
            
        case 2:

        case 3:

        case 4:

        case _:
            
# Open the JSON file
# with open("tienda.json") as file:
#     data = json.load(file)

# print (data)