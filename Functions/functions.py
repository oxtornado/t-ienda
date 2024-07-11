import json
import os
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display products in the store
def mostrar_productos(main):
    clear()
    with open(r"Json/9.json") as tienda:
        data = json.load(tienda)
    
    print('''
==================== Tienda Danielo's ====================
=============Los productos que manejamos son: ============
            ''')
    
    headers = ['Producto', 'Marca', 'Precio', 'Stock', 'Codigo']
    rows = [(p["producto"], p["marca"], str(p["precio"]), str(p["stock"]), str(p["codigo"])) for p in data]
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    print('-+-'.join('-' * length for length in max_lengths))
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))
    
    input("Volver al menu? (enter): ")
    main()

# Function to add products to the store
def ingresar_productos(main):
    clear()
    with open(r"Json/9.json") as tienda:
        data = json.load(tienda)
    
    print('''
==================== Tienda Danielo's ====================
=============Los productos que manejamos son: ============
            ''')
    
    headers = ['Producto', 'Marca', 'Precio', 'Stock', 'Codigo']
    rows = [(p["producto"], p["marca"], str(p["precio"]), str(p["stock"]), str(p["codigo"])) for p in data]
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    print('-+-'.join('-' * length for length in max_lengths))
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

    with open(r"Json/9.json", 'r') as tienda_file:
        data = json.load(tienda_file)
    
    while True:
        producto = input('Ingrese el nombre de su producto: ').title()
        marca = input('Ingrese la marca de su producto: ').title()
        precio = float(input('Ingrese el precio de su producto: ')) 
        stock = int(input('Ingrese el stock de su producto: '))  
        codigo = int(input('Ingrese el codigo de su producto: '))

        if any(item["producto"] == producto for item in data):
            print('El producto ya existe en la tienda, por favor ingrese otro producto')
            continue

        data.append({"producto": producto, "marca": marca, "precio": precio, "stock": stock, "codigo": codigo})
        print('Producto añadido!')
        
        if input("¿Desea ingresar otro producto? (s/enter): ").lower() != 's':
            clear()
            break
    
    with open(r"Json/9.json", 'w') as tienda_file:
        json.dump(data, tienda_file, indent=4)
    input("Volver al menu? (enter): ")
    main()

# Function to delete products from the store
def eliminar_producto(main):
    clear()
    with open(r"Json/9.json") as tienda:
        data = json.load(tienda)
    
    print('''
==================== Tienda Danielo's ====================
=============Los productos que manejamos son: ============
            ''')
    
    headers = ['Producto', 'Marca', 'Precio', 'Stock', 'Codigo']
    rows = [(p["producto"], p["marca"], str(p["precio"]), str(p["stock"]), str(p["codigo"])) for p in data]
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    print('-+-'.join('-' * length for length in max_lengths))
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

    delete_option = int(input("Ingrese el codigo del producto que desea eliminar: "))
    data = [item for item in data if item["codigo"] != delete_option]
    with open(r"Json/9.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"El producto con codigo '{delete_option}' ha sido eliminado.")
    input("Volver al menu? (enter): ")
    main()

# Function to display the cart
def mostrar_carrito(main):
    clear()
    with open("Json/carrito.json") as carrito_file:
        data = json.load(carrito_file)
    
    print('''
==================== Tienda Danielo's ====================
============= Su carrito contiene: ============
            ''')
    
    headers = ['Producto', 'Marca', 'Precio', 'Stock', 'Codigo']
    rows = [(p["producto"], p["marca"], str(p["precio"]), str(p["stock"]), str(p["codigo"])) for p in data]
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    print('-+-'.join('-' * length for length in max_lengths))
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))
    
    input("Volver al menu? (enter): ")
    main()

# Function to add products to the cart
def agregar_al_carrito(main):
    clear()
    with open(r"Json/9.json") as tienda:
        data = json.load(tienda)
    
    print('''
==================== Tienda Danielo's ====================
=============Puede agregar los siguiente productos: ============
            ''')
    
    headers = ['Producto', 'Marca', 'Precio', 'Stock', 'Codigo']
    rows = [(p["producto"], p["marca"], str(p["precio"]), str(p["stock"]), str(p["codigo"])) for p in data]
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    print('-+-'.join('-' * length for length in max_lengths))
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

    with open("Json/carrito.json", "r") as carrito_file:
        cart_data = json.load(carrito_file)

    while True:
        delete_option = input("Ingrese el codigo del producto que desea agregar al carrito: ").strip().title()
        producto_encontrado = False
        for item in data:
            if str(item["codigo"]) == delete_option:
                cantidad = int(input(f"Ingrese la cantidad de '{item['producto']}' que desea agregar al carrito: "))
                if cantidad <= item["stock"]:
                    item["stock"] -= cantidad
                    cart_data.append({
                        "producto": item["producto"],
                        "marca": item["marca"],
                        "precio": item["precio"],
                        "stock": cantidad,
                        "codigo": item["codigo"]
                    })
                    print(f"Se agregaron {cantidad} '{item['producto']}' al carrito.")
                    producto_encontrado = True
                else:
                    print(f"No hay suficiente stock disponible para {item['producto']}. Stock actual: {item['stock']}")
                break

        if not producto_encontrado:
            print(f"El producto con codigo '{delete_option}' no existe en la lista de productos disponibles.")
        
        if input("¿Desea ingresar otro producto? (s/n): ").lower() != 's':
            break

    with open("Json/carrito.json", "w") as carrito_file:
        json.dump(cart_data, carrito_file, indent=4)

    with open("Json/9.json", "w") as f:
        json.dump(data, f, indent=4)

    mostrar_carrito(main)

# Function to delete products from the cart
def eliminar_del_carrito(main):
    clear()
    mostrar_carrito(main)
    with open("Json/carrito.json", "r") as carrito_file:
        data = json.load(carrito_file)

    delete_option = input("Ingrese el codigo del producto que desea eliminar del carrito: ").strip().title()
    data = [item for item in data if str(item["codigo"]) != delete_option]
    with open("Json/carrito.json", "w") as carrito_file:
        json.dump(data, carrito_file, indent=4)
    print(f"El producto con codigo '{delete_option}' ha sido eliminado del carrito.")
    input("Volver al menu? (enter): ")
    main()

# Function to create backups
def crear_backup(main):
    clear()
    backup_dir = "Backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"backup_{timestamp}.json")
    
    with open(r"Json/9.json") as tienda_file:
        data = json.load(tienda_file)
    
    with open(backup_file, "w") as backup_file:
        json.dump(data, backup_file, indent=4)
    
    print(f"Backup creado exitosamente: {backup_file}")
    input("Volver al menu? (enter): ")
    main()

# Function to edit products in the store
def editar_producto(main):
    clear()
    with open(r"Json/9.json") as tienda:
        data = json.load(tienda)
    
    print('''
==================== Tienda Danielo's ====================
============= Los productos que manejamos son: ============
            ''')
    
    headers = ['Producto', 'Marca', 'Precio', 'Stock', 'Codigo']
    rows = [(p["producto"], p["marca"], str(p["precio"]), str(p["stock"]), str(p["codigo"])) for p in data]
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    print('-+-'.join('-' * length for length in max_lengths))
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))
    
    codigo = input("Ingrese el codigo del producto que desea editar: ").strip().title()
    for item in data:
        if str(item["codigo"]) == codigo:
            print(f"Editando producto: {item['producto']}")
            item["producto"] = input(f"Nuevo nombre del producto ({item['producto']}): ").title() or item["producto"]
            item["marca"] = input(f"Nuevo marca del producto ({item['marca']}): ").title() or item["marca"]
            item["precio"] = float(input(f"Nuevo precio del producto ({item['precio']}): ") or item["precio"])
            item["stock"] = int(input(f"Nuevo stock del producto ({item['stock']}): ") or item["stock"])
            break
    else:
        print(f"No se encontró ningún producto con el código '{codigo}'.")

    with open(r"Json/9.json", "w") as tienda_file:
        json.dump(data, tienda_file, indent=4)
    print("Producto editado con éxito.")
    input("Volver al menu? (enter): ")
    main()
