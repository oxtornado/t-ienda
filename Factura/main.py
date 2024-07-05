import jinja2
import pdfkit
import os
import json

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
        'Cantidad',  # Changed from 'Stock' to 'Cantidad' (Quantity)
        'Codigo'
    ]
    
    rows = []
    for product in data:
        rows.append((
            product["producto"],
            product["marca"],
            str(product["precio"]),  
            str(product["stock"]),  # Update this to reflect 'cantidad' instead of 'stock'
            str(product["codigo"])   
        ))
    
    max_lengths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    
    print(' | '.join(f"{header.ljust(max_lengths[i])}" for i, header in enumerate(headers)))
    print('-+-'.join('-' * length for length in max_lengths))
    
    for row in rows:
        print(' | '.join(f"{str(item).ljust(max_lengths[i])}" for i, item in enumerate(row)))

    return data  # Return updated cart data



def crea_pdf(ruta_template, info, ruta_css=''):
    nombre_template = os.path.basename(ruta_template)
    ruta_template = os.path.dirname(ruta_template)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)
    
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8'
    }
    
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    ruta_salida = r'C:\Users\danie\P\tienda\Factura\factura.pdf'  # Ensure this path exists

    pdfkit.from_string(html, ruta_salida, css=ruta_css, options=options, configuration=config)
