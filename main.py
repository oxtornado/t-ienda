import json
from Functions.functions import *
from Factura.main import *
#Funcion encargada de mostrar el menu de la tienda
def main():
    clear()
    while True:
        try:
            #Imprimimos el menu
            print('''
        ==================== Tienda Danielo's ====================
        =============Bienvenido, a continuacion puede: ===========
                    | 1. Mostrar lista de productos
                    | 2. Agregar un producto
                    | 3. Eliminar un producto
                    | 4. Agregar Producto(s) al Carrito
                    | 5. Eliminar Producto(s) del Carrito
                    | 6. Mostrar Carrito
                    | 7. Comprar Carrito
                    | 8. Salir
        ==========================================================
        ''')
            
            # Preguntamos que opcion queiere llevar a cabo
            primer_input = int(input('Ingrese el numero de la accion que desa llevar a cabo: '))
            
            # Control de la respuesta con un match porque es una estructura de control 
            # excelente para el control de casos especificos
            match primer_input:
                case 1:
                    mostrar_productos(main)
                case 2:
                    ingresar_productos(main)
                case 3:
                    eliminar_producto(main)
                case 4:
                    agregar_al_carrito(main)
                case 5:
                    eliminar_del_carrito(main)
                case 6:
                    mostrar_carrito(main)
                case 7:
                    ruta_template = os.path.abspath('index.html')
                    
                    # Get the cart data
                    lista_carrito = mostrar_carrito()
                    
                    # Prepare info dictionary for PDF generation
                    info = {"lista_de_productos_para_factura": lista_carrito}
                    
                    # Call crea_pdf with the correct info
                    crea_pdf(ruta_template, info)
                case 8:
                    exit()
                case _:
                    print('Opcion no valida, vuelva a intentarlo')
                    continue
        except ValueError as e:
            print(f'Error!: {e}')
        clear()
if __name__ == "__main__":
    main()