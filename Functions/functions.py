import json
from clases import *

def mostrar_productos():
    with open("lista_de_productos.json") as tienda:
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
      # Construct rows as a list of tuples
    rows = [
          (
            data["producto"],

          )
      ]

      # Calculate max_lengths using zip to transpose the headers and rows
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    # Print headers
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    
    # Print separator
    print('-+-'.join('-' * length for length in max_lengths))
    
    # Print rows
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

if __name__ == '__main__':
    mostrar_productos()
