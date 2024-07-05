import json
import os
from clases import *  


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Funcion encargada de mostrar los productos de la tienda
def mostrar_productos(main):
    clear()
    with open(r"Json\9.json") as tienda:
        data = json.load(tienda)
    
    print('''
==================== Tienda Danielo's ====================
=============Los productos que manejamos son: ============
            ''')
    
    headers = [
        'Producto',
        'Marca',
        'Precio',
        'Stock',
        'Codigo'
    ]
    
    rows = []
    for product in data:
        rows.append((
            product["producto"],
            product["marca"],
            str(product["precio"]),  
            str(product["stock"]),   
            str(product["codigo"])   
        ))
    
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    
    print('-+-'.join('-' * length for length in max_lengths))
    
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))
    while True:
        #Preguntamos si desea continuar
        continuar = input("Volver al menu? (s/n): ")

        #Si al respuesta es difernte de la opcion si, se rompe el ciclo
        if continuar.lower() != 's':
            break
        else:
            main()

#Funcion encargada de la creacion de productos de la tienda
def ingresar_productos(main):
    clear()

    mostrar_productos(main)

    #Lllamamos la lista que esta en la direccion 'Json\9.json' como tienda_file
    with open(r"Json\9.json", 'r') as tienda_file:


        #La compilacion de los datos se va a llamar data
        data = json.load(tienda_file)
    
    #Bucle para el ingreso de productos 
    while True:

        #Nombramos los atributos de los productos para que el usuario los vaya nombrando
        producto = input('Ingrese el nombre de su producto: ').title()
        marca = input('Ingrese la marca de su producto: ').title()
        precio = float(input('Ingrese el precio de su producto: ')) 
        stock = int(input('Ingrese el stock de su producto: '))  
        codigo = int(input('Ingrese el codigo de su producto: '))

        #Creamos una variable que se encargue de recorrer la lista y nos diga si 
        # ese elemento que queremos agregar exite ya en la lista JSON
        producto_existente = False

        # La variable que creamos va a recorrer la lista y cambiara su valor 
        # si el nombre del porducto que queremos crear existe ya o no
        for item in data:

            #Creamos la condicion para que cambie su valor
            if item["producto"] == producto:
                producto_existente = True
                #Terminamos el recorrido si encuentra un elemento con el mismo nombre
                break
        # Si es verdadero imprimimos un mensaje avisando al usuario
        if producto_existente:
            print('El producto ya existe en la tienda, por favor ingrese otro producto')
            # Al imprimirse el mensaje continuamos hasta que ingrese un producto valido
            continue

        # Pero si de lo contrario, no encuentra el producto
        else:
            #Agregamos el producto a la lista JSON
            data.append({
                "producto": producto,
                "marca": marca,
                "precio": precio,
                "stock": stock,
                "codigo": codigo
            })
        # terminamos (si es el caso) avisando que ya se subio el producto
        print('Producto añadido!')
        
        #Preguntamos si desea continuar
        continuar = input("¿Desea ingresar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break
    #Subimos el nuevo porducto a la lista
    with open(r"Json\9.json", 'w') as tienda_file:
        json.dump(data, tienda_file, indent=4)

    while True:
        #Preguntamos si desea continuar
        continuar = input("Volver al menu? (s/n): ")

        #Si al respuesta es difernte de la opcion si, se rompe el ciclo
        if continuar.lower() != 's':
            break
        else:
            main()

#Funcion encargada de eliminar productos de la tienda
def eliminar_producto(main):
    mostrar_productos(main)  # Display current products

    # Load existing data from JSON file
    with open(r"Json\9.json", "r") as f:
        data = json.load(f)

    while True:
        delete_option = input("Ingrese el nombre del producto que desea eliminar (o '0' para salir): ").strip().title()

        if delete_option == '0':
            break

        producto_encontrado = False
        for item in data:
            if item["producto"] == delete_option:
                data.remove(item)
                producto_encontrado = True
                print(f"El producto '{delete_option}' ha sido eliminado.")
                break

        if not producto_encontrado:
            print(f"El producto '{delete_option}' no existe en la lista.")

    # Save updated data back to JSON file
    with open(r"Json\9.json", "w") as f:
        json.dump(data, f, indent=4)

    mostrar_productos(main)  # Display updated list of products after deletion
    

    mostrar_productos(main)   # Lista actualizada con los cambios que se le hayan hecho
    while True:
        #Preguntamos si desea continuar
        continuar = input("Volver al menu? (s/n): ")

        #Si al respuesta es difernte de la opcion si, se rompe el ciclo
        if continuar.lower() != 's':
            break
        else:
            main()


def mostrar_carrito(main):
    with open("Json/carrito.json") as carrito_file:
        data = json.load(carrito_file)
    
    print('''
==================== Tienda Danielo's ====================
============= Su carrito contiene: ============
            ''')
    
    headers = [
        'Producto',
        'Marca',
        'Precio',
        'Stock',
        'Codigo'
    ]
    
    rows = []
    for product in data:
        rows.append((
            product["producto"],
            product["marca"],
            str(product["precio"]),  
            str(product["stock"]),   
            str(product["codigo"])   
        ))
    
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    print('-+-'.join('-' * length for length in max_lengths))
    
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))
    
    while True:
        #Preguntamos si desea continuar
        continuar = input("Volver al menu? (s/n): ")

        #Si al respuesta es difernte de la opcion si, se rompe el ciclo
        if continuar.lower() != 's':
            break
        else:
            main()


def agregar_al_carrito(main):
    clear()
    mostrar_productos(main)  # Display available products

    # Load product data from the main product file (assuming it's named '9.json')
    with open("Json/9.json", "r") as f:
        data = json.load(f)

    # Load cart data
    with open("Json/carrito.json", "r") as carrito_file:
        cart_data = json.load(carrito_file)

    while True:
        delete_option = input("Ingrese el nombre del producto que desea agregar al carrito: ").strip().title()

        if delete_option:  # Check if user entered something
            producto_encontrado = False
            for item in data:
                if item["producto"] == delete_option:
                    cantidad = int(input(f"Ingrese la cantidad de '{delete_option}' que desea agregar al carrito: "))
                    if cantidad <= item["stock"]:
                        item["stock"] -= cantidad
                        cart_data.append({
                            "producto": item["producto"],
                            "marca": item["marca"],
                            "precio": item["precio"],
                            "stock": cantidad,
                            "codigo": item["codigo"]
                        })
                        print(f"Se agregaron {cantidad} '{delete_option}' al carrito.")
                        producto_encontrado = True
                    else:
                        print(f"No hay suficiente stock disponible para {delete_option}. Stock actual: {item['stock']}")
                    break

            if not producto_encontrado:
                print(f"El producto '{delete_option}' no existe en la lista de productos disponibles.")

        continuar = input("¿Desea ingresar otro producto? (s/n): ")

        if continuar.lower() != 's':
            break

    # Update and save the cart data
    with open("Json/carrito.json", "w") as carrito_file:
        json.dump(cart_data, carrito_file, indent=4)

    # Update and save the main product data with updated stock
    with open("Json/9.json", "w") as f:
        json.dump(data, f, indent=4)

    clear()

    mostrar_carrito(main)  # Display updated cart after additions
    while True:
        #Preguntamos si desea continuar
        continuar = input("Volver al menu? (s/n): ")

        #Si al respuesta es difernte de la opcion si, se rompe el ciclo
        if continuar.lower() != 's':
            break
        else:
            main()


def eliminar_del_carrito(main):

    clear()

    mostrar_carrito(main)

    with open("Json/carrito.json", "r") as carrito_file:
        data = json.load(carrito_file)

    while True:
        delete_option = input("Ingrese el nombre del producto que desea eliminar del carrito (o '0' para salir): ").strip().title()

        if delete_option == '0':
            break

        producto_encontrado = False
        for product in data:
            if product["producto"] == delete_option:
                data.remove(product)
                producto_encontrado = True
                print(f"El producto '{delete_option}' ha sido eliminado del carrito.")
                break

        if not producto_encontrado:
            print(f"El producto '{delete_option}' no existe en el carrito.")

    with open("Json/carrito.json", "w") as carrito_file:
        json.dump(data, carrito_file, indent=4)

    while True:
        #Preguntamos si desea continuar
        continuar = input("Volver al menu? (s/n): ")

        #Si al respuesta es difernte de la opcion si, se rompe el ciclo
        if continuar.lower() != 's':
            break
        else:
            main()

# if __name__ == "__main__":
#     eliminar_del_carrito()
#     # eliminar_producto()
#     # # ingresar_productos()
#     # mostrar_productos()