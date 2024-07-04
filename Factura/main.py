import jinja2
import pdfkit
import os
import json

def mostrar_carrito():
    with open("Json/carrito.json") as carrito_file:
        data = json.load(carrito_file)
    
    products = []
    for product in data:
        product_info = {
            'producto': product["producto"],
            'marca': product["marca"],
            'precio': str(product["precio"]),
            'stock': str(product["stock"]),
            'codigo': str(product["codigo"])
        }
        products.append(product_info)
    
    return products



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
