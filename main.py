from Functions.functions import *
from Factura.main import *

def main():
    while True:
        print('''
==================== Tienda Danielo's ====================
============= Elige la opción que deseas: ================
1.- Ver productos disponibles
2.- Ingresar nuevos productos
3.- Eliminar productos
4.- Ver carrito de compras
5.- Agregar productos al carrito
6.- Eliminar productos del carrito
7.- Crear un backup de la tienda
8.- Editar productos
9.- Imprimir factura
10.- Salir
        ''')
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            mostrar_productos(main)
        elif opcion == '2':
            ingresar_productos(main)
        elif opcion == '3':
            eliminar_producto(main)
        elif opcion == '4':
            mostrar_carrito(main)
        elif opcion == '5':
            agregar_al_carrito(main)
        elif opcion == '6':
            eliminar_del_carrito(main)
        elif opcion == '7':
            crear_backup(main)
        elif opcion == '8':
            editar_producto(main)
        elif opcion == '9':
            ruta_template = os.path.abspath('index.html')
            lista_carrito = mostrar_carrito()
            subtotal = sum(item["precio"] * item["stock"] for item in lista_carrito)
            total = subtotal * 1.12  # Assuming a 12% tax rate
            info = {
                "lista_de_productos_para_factura": lista_carrito,
                "subtotal": subtotal,
                "total": total
            }
            crea_pdf(ruta_template, info)
        elif opcion == '10':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor ingrese una opción válida.")

if __name__ == "__main__":
    main()