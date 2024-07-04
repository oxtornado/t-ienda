import json
from clases import *  


#Funcion encargada de mostrar los productos de la tienda
def mostrar_productos():
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


#Funcion encargada de la creacion de productos de la tienda
def ingresar_productos():

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


#Funcion encargada de eliminar productos de la tienda
def eliminar_producto():

    mostrar_productos()  # Assuming mostrar_productos() displays the current products

    # Load existing data from JSON file
    with open(r"Json\9.json", "r") as f:
        data = json.load(f)

    while True:
        print("Ingrese el nombre del producto que desea eliminar:") # Aviso para que el usuario sepa que hacer
        delete_option = input(" ").strip().title()  # Input para digitiar el nombre del producto

        if delete_option: # Creamos una condicion que siempre se lleve a cabo
            
            # Creamos una variable de control que lea la lista de productos y cambie su valor si encuentra 'delete_option'
            producto_existente = False

            #Aqui creamos el bucle para que recorra la lista 
            for item in data:

                
            #Pero tambien  
                if not producto_existente:
                    print(f"El producto '{delete_option}' no existe en la lista.")
                    continue

                # Si el producto que digito el usuario es el mismo que el que se encuentra en la lista
                if item["producto"] == delete_option:

                    #Lo eliminaremos
                    data.remove(item)
                    
                    # Y cambiaremos el valor de la variable 
                    producto_existente = True

                    # Imprimimos un aviso de que el producto ha sido eliminado
                    print(f"El producto '{delete_option}' ha sido eliminado.")

                    #Rompemos el ciclo
                    break


        #Preguntamos si desea continuar
        continuar = input("¿Desea ingresar otro producto? (s/n): ")

        #Si al respuesta es difernte de la opcion si, se rompe el ciclo
        if continuar.lower() != 's':
            break

    # Se sube la lista de nuevo y a continuacion se muestra la lista actualizada
    with open(r"Json\9.json", "w") as f:
        json.dump(data, f, indent=4)
    
    mostrar_productos()   # Lista actualizada con los cambios que se le hayan hecho

def mostrar_carrito():
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

def agregar_al_carrito():

    mostrar_productos()  # Display available products

    # Load product data from the main product file (assuming it's named '9.json')
    with open("Json/9.json", "r") as f:
        data = json.load(f)

    # Initialize cart data list
    data_c = []

    while True:
        delete_option = input("Ingrese el nombre del producto que desea agregar al carrito: ").strip().title()

        if delete_option:  # Check if user entered something
            producto_existente = False
            
            for item in data:
                if item["producto"] == delete_option:
                    data_c.append(item)  # Add selected product to cart data
                    producto_existente = True
                    print(f"El producto '{delete_option}' ha sido agregado al carrito de compras.")
                    break

            if not producto_existente:
                print(f"El producto '{delete_option}' no existe en la lista de productos disponibles.")

        continuar = input("¿Desea ingresar otro producto? (s/n): ")

        if continuar.lower() != 's':
            break
    
    # Update and save the cart data
    with open("Json/carrito.json", "w") as carrito_file:
        json.dump(data_c, carrito_file, indent=4)
    
    mostrar_carrito()  # Display updated cart after additions

def eliminar_del_carrito():
    mostrar_carrito()

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


if __name__ == "__main__":
    eliminar_del_carrito()
    # eliminar_producto()
    # # ingresar_productos()
    # mostrar_productos()